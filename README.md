# BookGenreOrganizer

BookGenreOrganizer is a tool designed to automatically categorize ePub and PDF books into genre-specific folders based on their metadata. The tool fetches genre information from the Google Books API and organizes the books into folders named after their genres.

## Features

- Automatically extracts metadata from ePub and PDF files.
- Fetches genre information using the Google Books API.
- Organizes books into genre-specific folders.
- Creates new folders if a genre folder does not already exist.

## Download .exe

https://github.com/sandeepbanoula/BookGenreOrganizer/BookGenreOrganizer.exe

## Requirements

- Python 3.6+
- The following Python libraries:
  - `ebooklib`
  - `PyPDF2`
  - `requests`

## Installation

To use this tool, you need to have Python and the required libraries installed. Follow the steps below to set up and run the tool.

### Step 1: Clone the Repository

Clone the repository to your local machine using:

```bash
git clone https://github.com/sandeepbanoula/BookGenreOrganizer.git
cd BookGenreOrganizer
```

### Step 2: Install Dependencies

Install the required Python libraries using pip:

```bash
pip install -r requirements.txt
```

## Usage

Copy the script to your books directory and run it inside your books directory:

```bash
python script.py
```

## Creating an Executable

If you want to create a standalone executable for easier distribution, follow these steps:

### Step 1: Install PyInstaller

Install PyInstaller if you haven't already:

```bash
pip install pyinstaller
```

### Step 2: Create the Executable

Run the following command to create a standalone executable:

```bash
pyinstaller --onefile script.py
```

The executable will be generated in the `dist` folder.

## Usage Instructions for Executable

1. **Download the Executable:**
   Download/Copy the `script.exe` file from the `dist` folder.

2. **Prepare Your Books Folder:**
   Ensure all your ePub and PDF files are in a single directory. For example, create a folder named `books` on your desktop and move all your ePub and PDF files into this folder.

3. **Run the Executable:**
   - Copy the executable file in the Books Folder and open it.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please create an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

<table>
  <tr>
    <td align="center"><a href="https://github.com/sandeepbanoula" target="_blank"><img src="https://avatars.githubusercontent.com/u/65235940?v=4" width="100px;" alt=""/><br /><sub><b>Sandeep Banoula</b></sub></a><br /></td>
  </tr>
</table>

## Acknowledgments

- Thanks to the developers of `ebooklib`, `PyPDF2`, and `requests` for their excellent libraries.
- Special thanks to Google Books API for providing the genre information.
- Thanks to ChatGPT by OpenAI for its help.