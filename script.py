import os
import requests
from ebooklib import epub
import PyPDF2
import shutil

# Function to extract metadata from ePub files
def get_epub_metadata(file_path):
    book = epub.read_epub(file_path)
    title = book.get_metadata('DC', 'title')[0][0]
    return title

# Function to extract metadata from PDF files
def get_pdf_metadata(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        info = reader.metadata
        title = info.get('/Title', os.path.basename(file_path))
    return title

# Function to fetch genre from Google Books API
def fetch_genre(title):
    query = "+".join(title.split())
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}"
    response = requests.get(url)
    data = response.json()
    
    try:
        # Extract the genre from the Google Books API response
        genre = data['items'][0]['volumeInfo']['categories'][0]
    except (KeyError, IndexError):
        genre = 'Unknown'

    return genre

# Function to organize files into genre folders
def organize_files_by_genre(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if filename.endswith('.epub'):
            title = get_epub_metadata(file_path)
        elif filename.endswith('.pdf'):
            title = get_pdf_metadata(file_path)
        else:
            continue

        genre = fetch_genre(title)
        genre_folder = os.path.join(directory, genre)
        
        if not os.path.exists(genre_folder):
            os.makedirs(genre_folder)

        shutil.move(file_path, os.path.join(genre_folder, filename))

if __name__ == "__main__":
    directory = './'
    organize_files_by_genre(directory)
