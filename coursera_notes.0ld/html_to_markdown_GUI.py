import tkinter as tk
from tkinter import scrolledtext
import html2text
from bs4 import BeautifulSoup
import re

verbose = False
verbose_code_block = False
verbose_html2text = False
verbose_replacement = False
verbose_clean_steps = False

def extract_html_to_markdown(html):
    soup = BeautifulSoup(html, 'html.parser')
    
    # Remove the unwanted information div
    for div in soup.find_all('div', class_='cds-347'):
        div.decompose()
    
    # Handle code blocks first
    for code_block in soup.find_all('div', class_='rc-CodeBlock'):
        view_lines = code_block.find_all('div', class_='view-line')
        code_lines = [line.get_text(strip=True) for line in view_lines]
        formatted_code = "\n<br>".join(code_lines)
        if verbose or verbose_code_block:
            print(formatted_code)
        # Replace the code block with a placeholder
        code_block.replace_with(f"CODEBLOCK_PLACEHOLDER{formatted_code}CODEBLOCK_PLACEHOLDER")
        if verbose:
            print(code_block)
    
    # Convert the rest of the HTML to Markdown
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = True
    h.body_width = 0
    markdown = h.handle(str(soup))
    if verbose or verbose_html2text:
        print(markdown)
    
    # Replace placeholders with properly formatted code blocks
    markdown = re.sub(r'CODEBLOCK_PLACEHOLDER(.*?)CODEBLOCK_PLACEHOLDER', 
                      lambda m: f"\n```python\n{m.group(1)}\n```\n", 
                      markdown, flags=re.DOTALL)
    if verbose or verbose_replacement:
        print(markdown)
    
    return markdown

def clean_note_content(content):
    # Remove line numbers
    content = re.sub(r'^\s*\d+\s*', '', content, flags=re.MULTILINE)
    if verbose or verbose_clean_steps:
        print(content)   
    # Remove any remaining instances of the unwanted text
    content = re.sub(r'Information:.*?Control\+M\.', '', content, flags=re.DOTALL)
    if verbose or verbose_clean_steps:
        print(content)    
    # Remove any extra newlines between code blocks and content
    content = re.sub(r'\n{3,}', '\n\n', content)
    if verbose or verbose_clean_steps:
        print(content)
    content = re.sub(r'<br>', '\n', content)
    if verbose or verbose_clean_steps:
        print(content)
    return content.strip()

def convert():
    html_content = input_text.get("1.0", tk.END)
    markdown_output = extract_html_to_markdown(html_content)
    cleaned_content = clean_note_content(markdown_output)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, cleaned_content)

def clear_input():
    input_text.delete("1.0", tk.END)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(output_text.get("1.0", tk.END))
    root.update()

# Create main window
root = tk.Tk()
root.title("HTML to Markdown Converter")
root.geometry("800x600")

# Input area
input_label = tk.Label(root, text="Paste your HTML here:")
input_label.pack()
input_text = scrolledtext.ScrolledText(root, width=80, height=15)
input_text.pack()

# Enable right-click paste for input area
input_text.bind("<Button-3>", lambda e: input_text.event_generate("<<Paste>>"))

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

convert_button = tk.Button(button_frame, text="Convert", command=convert)
convert_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(button_frame, text="Clear", command=clear_input)
clear_button.pack(side=tk.LEFT, padx=5)

# Output area
output_label = tk.Label(root, text="Converted Markdown:")
output_label.pack()
output_text = scrolledtext.ScrolledText(root, width=80, height=15)
output_text.pack()

# Copy to clipboard button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=10)

# Enable right-click copy for output area
output_text.bind("<Button-3>", lambda e: output_text.event_generate("<<Copy>>"))

root.mainloop()