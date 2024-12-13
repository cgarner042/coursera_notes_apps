import tkinter as tk
from tkinter import ttk, scrolledtext
import re
import html2text
from bs4 import BeautifulSoup

def remove_timestamps():
    input_text = timestamp_input.get("1.0", tk.END)
    cleaned_text = re.sub(r'^Play .*', '', input_text, flags=re.MULTILINE)
    timestamp_output.delete("1.0", tk.END)
    timestamp_output.insert(tk.END, cleaned_text)

def clear_timestamp():
    timestamp_input.delete("1.0", tk.END)
    timestamp_output.delete("1.0", tk.END)

def copy_timestamp():
    root.clipboard_clear()
    root.clipboard_append(timestamp_output.get("1.0", tk.END))
    root.update()

def extract_html_to_markdown(html):
    soup = BeautifulSoup(html, 'html.parser')
    
    for div in soup.find_all('div', class_='cds-347'):
        div.decompose()
    
    for code_block in soup.find_all('div', class_='rc-CodeBlock'):
        view_lines = code_block.find_all('div', class_='view-line')
        code_lines = [line.get_text(strip=False) for line in view_lines]
        formatted_code = "\n<br>".join(code_lines)
        code_block.replace_with(f"CODEBLOCK_PLACEHOLDER{formatted_code}CODEBLOCK_PLACEHOLDER")
    
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = True
    h.body_width = 0
    markdown = h.handle(str(soup))
    
    markdown = re.sub(r'CODEBLOCK_PLACEHOLDER(.*?)CODEBLOCK_PLACEHOLDER', 
                      lambda m: f"\n```python\n{m.group(1)}\n```\n", 
                      markdown, flags=re.DOTALL)
    
    return markdown

def clean_note_content(content):
    content = re.sub(r'^\s*\d+\s*', '', content, flags=re.MULTILINE)
    content = re.sub(r'Information:.*?Control\+M\.', '', content, flags=re.DOTALL)
    content = re.sub(r'\n{3,}', '\n\n', content)
    content = re.sub(r'<br>', '\n', content)
    return content.strip()

def convert_markdown():
    html_content = markdown_input.get("1.0", tk.END)
    markdown_output = extract_html_to_markdown(html_content)
    cleaned_content = clean_note_content(markdown_output)
    markdown_output_text.delete("1.0", tk.END)
    markdown_output_text.insert(tk.END, cleaned_content)

def clear_markdown():
    markdown_input.delete("1.0", tk.END)
    markdown_output_text.delete("1.0", tk.END)

def copy_markdown():
    root.clipboard_clear()
    root.clipboard_append(markdown_output_text.get("1.0", tk.END))
    root.update()



# Create main window
root = tk.Tk()
root.title("Coursera Notes App")
root.geometry("1200x800")

# Make root window expandable
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Create custom styles
style = ttk.Style()
style.theme_use('default')

# Configure notebook tab style
style.configure("TNotebook.Tab", padding=[10, 5], font=('Helvetica', 12, 'bold'))
style.map("TNotebook.Tab", 
          background=[("selected", "#4CAF50"), ("active", "#81C784")],
          foreground=[("selected", "white"), ("active", "black")])

# Configure button style
style.configure("TButton", padding=10, font=('Helvetica', 11, 'bold'), 
                background="#2196F3", foreground="white")
style.map("TButton", 
          background=[("active", "#64B5F6")],
          relief=[("pressed", "sunken"), ("!pressed", "raised")])

# Create a notebook (tabbed interface)
notebook = ttk.Notebook(root)
notebook.grid(row=0, column=0, sticky="nsew")

# Timestamp Remover Tab
timestamp_frame = ttk.Frame(notebook)
notebook.add(timestamp_frame, text='Timestamp Remover')

timestamp_frame.columnconfigure(0, weight=1)
timestamp_frame.rowconfigure(1, weight=1)
timestamp_frame.rowconfigure(3, weight=1)

timestamp_input_label = ttk.Label(timestamp_frame, text="Input Text:", font=('Helvetica', 12))
timestamp_input_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

timestamp_input = scrolledtext.ScrolledText(timestamp_frame, font=('Helvetica', 11))
timestamp_input.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

timestamp_output_label = ttk.Label(timestamp_frame, text="Output Text:", font=('Helvetica', 12))
timestamp_output_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)

timestamp_output = scrolledtext.ScrolledText(timestamp_frame, font=('Helvetica', 11))
timestamp_output.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)

timestamp_button_frame = ttk.Frame(timestamp_frame)
timestamp_button_frame.grid(row=4, column=0, pady=10)

remove_button = ttk.Button(timestamp_button_frame, text="Remove Timestamps", command=remove_timestamps, style="TButton")
remove_button.pack(side=tk.LEFT, padx=5)

copy_timestamp_button = ttk.Button(timestamp_button_frame, text="Copy to Clipboard", command=copy_timestamp, style="TButton")
copy_timestamp_button.pack(side=tk.LEFT, padx=5)

clear_timestamp_button = ttk.Button(timestamp_button_frame, text="Clear", command=clear_timestamp, style="TButton")
clear_timestamp_button.pack(side=tk.LEFT, padx=5)

# Markdown Converter Tab
markdown_frame = ttk.Frame(notebook)
notebook.add(markdown_frame, text='Markdown Converter')

markdown_frame.columnconfigure(0, weight=1)
markdown_frame.rowconfigure(1, weight=1)
markdown_frame.rowconfigure(3, weight=1)

markdown_input_label = ttk.Label(markdown_frame, text="Paste your HTML here:", font=('Helvetica', 12))
markdown_input_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

markdown_input = scrolledtext.ScrolledText(markdown_frame, font=('Helvetica', 11))
markdown_input.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

markdown_output_label = ttk.Label(markdown_frame, text="Converted Markdown:", font=('Helvetica', 12))
markdown_output_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)

markdown_output_text = scrolledtext.ScrolledText(markdown_frame, font=('Helvetica', 11))
markdown_output_text.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)

markdown_button_frame = ttk.Frame(markdown_frame)
markdown_button_frame.grid(row=4, column=0, pady=10)

convert_button = ttk.Button(markdown_button_frame, text="Convert", command=convert_markdown, style="TButton")
convert_button.pack(side=tk.LEFT, padx=5)

copy_markdown_button = ttk.Button(markdown_button_frame, text="Copy to Clipboard", command=copy_markdown, style="TButton")
copy_markdown_button.pack(side=tk.LEFT, padx=5)

clear_markdown_button = ttk.Button(markdown_button_frame, text="Clear", command=clear_markdown, style="TButton")
clear_markdown_button.pack(side=tk.LEFT, padx=5)

# Enable right-click paste for input areas
timestamp_input.bind("<Button-3>", lambda e: timestamp_input.event_generate("<<Paste>>"))
markdown_input.bind("<Button-3>", lambda e: markdown_input.event_generate("<<Paste>>"))

# Enable right-click copy for output areas
timestamp_output.bind("<Button-3>", lambda e: timestamp_output.event_generate("<<Copy>>"))
markdown_output_text.bind("<Button-3>", lambda e: markdown_output_text.event_generate("<<Copy>>"))

root.mainloop()
