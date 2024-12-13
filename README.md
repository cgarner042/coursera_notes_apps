# Coursera Notes App

The Coursera Notes App is a Tkinter-based application designed to assist users in managing their notes from Coursera courses. It provides functionalities for removing timestamps from video transcripts and converting HTML content from readings to Markdown.

## Features

- **Timestamp Remover**: Removes timestamps from input text and provides a cleaned version.
- **Markdown Converter**: Converts HTML content to Markdown, cleaning up the content and formatting code blocks.

## Requirements

- Python 3.x
- Tkinter
- BeautifulSoup4
- html2text

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/undeadcycle/coursera_notes_app.git
    cd coursera_notes_app
    ```

2. **Install the required packages**:
    ```bash
    pip install beautifulsoup4 html2text
    ```

## Usage

1. **Run the application**:
    ```bash
    python coursera_notes_app.py
    ```

2. **Using the Timestamp Remover**:
    - Copy any section of the video transcript to your clipboard
    - Navigate to the "Timestamp Remover" tab.
    - Paste your text with timestamps in the "Input Text" field.
    - Click "Remove Timestamps" to clean the text.
    - The cleaned text will appear in the "Output Text" field.
    - You can copy the cleaned text to the clipboard or clear the fields using the provided buttons.

3. **Using the Markdown Converter**:
    - Find the section of the reading that you want to save and right-click inspect element. 
    - Make sure that it contains all of the content you require and copy element
    - Navigate to the "Markdown Converter" tab.
    - Paste your HTML content in the "Paste your HTML here" field.
    - Click "Convert" to convert the HTML to Markdown.
    - The converted Markdown will appear in the "Converted Markdown" field.
    - You can copy the Markdown to the clipboard or clear the fields using the provided buttons.

## File Structure

coursera-notes-app/
│
├── coursera_notes_app.py # Main application file
├── README.md # This README file
└── coursera_notes_app.desktop # For easier launching on linux systems (will require the path to be set correctly on the exec line) 


## Functions

### `remove_timestamps`
Removes timestamps from the input text.

### `clear_timestamp`
Clears the input and output fields in the Timestamp Remover tab.

### `copy_timestamp`
Copies the cleaned text from the Timestamp Remover tab to the clipboard.

### `extract_html_to_markdown`
Converts HTML content to Markdown, with specific handling for Coursera notes.

### `clean_note_content`
Cleans up the note content, removing unnecessary information and formatting.

### `convert_markdown`
Converts the HTML content in the Markdown Converter tab to Markdown and displays it.

### `clear_markdown`
Clears the input and output fields in the Markdown Converter tab.

### `copy_markdown`
Copies the converted Markdown from the Markdown Converter tab to the clipboard.

## Custom Styles

- **Notebook Tab Style**: Customized appearance for notebook tabs.
- **Button Style**: Customized appearance for buttons.

## Right-Click Functionality

- **Input Areas**: Right-click to paste content.
- **Output Areas**: Right-click to copy content.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Author

- Christopher Garner
- [undeadcycle](https://github.com/undeadcycle)

