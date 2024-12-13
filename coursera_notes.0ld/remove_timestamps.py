#!/usr/bin/env python

import re
import tkinter as tk
from tkinter import scrolledtext

def remove_timestamps():
    input_text = input_text_area.get("1.0", tk.END)
    cleaned_text = re.sub(r'^Play .*', '', input_text, flags=re.MULTILINE)
    output_text_area.delete("1.0", tk.END)
    output_text_area.insert(tk.END, cleaned_text)

def copy_to_clipboard():
    output_text = output_text_area.get("1.0", tk.END)
    root.clipboard_clear()
    root.clipboard_append(output_text)
    root.update()  # This is necessary to finalize the clipboard update

def clear_input():
    input_text_area.delete("1.0", tk.END)

# Create main window
root = tk.Tk()
root.title("Timestamp Remover")
root.geometry("600x400")

# Create input text area
input_label = tk.Label(root, text="Input Text:")
input_label.pack()
input_text_area = scrolledtext.ScrolledText(root, width=70, height=10)
input_text_area.pack()

# Enable right-click paste for input area
input_text_area.bind("<Button-3>", lambda e: input_text_area.event_generate("<<Paste>>"))

# Create output text area
output_label = tk.Label(root, text="Output Text:")
output_label.pack()
output_text_area = scrolledtext.ScrolledText(root, width=70, height=10)
output_text_area.pack()

# Enable right-click copy for output area
output_text_area.bind("<Button-3>", lambda e: output_text_area.event_generate("<<Copy>>"))

# Create buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

remove_button = tk.Button(button_frame, text="Remove Timestamps", command=remove_timestamps)
remove_button.pack(side=tk.LEFT, padx=5)

copy_button = tk.Button(button_frame, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(button_frame, text="Clear Input", command=clear_input)
clear_button.pack(side=tk.LEFT, padx=5)

# Start the GUI event loop
root.mainloop()