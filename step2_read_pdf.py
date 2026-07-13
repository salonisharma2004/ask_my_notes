#read and seperate the content into chunks
from pypdf import PdfReader

def read_pdf(filepath):
    reader = PdfReader(filepath)
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text() + "\n"
    return full_text

def split_into_chunks(text, chunk_size=500):
    # breaks the text into pieces of roughly chunk_size characters each
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])
    return chunks

# --- Program starts here ---
filename = input("Enter your PDF filename (e.g. notes.pdf): ")
text = read_pdf(filename)
print(f"\nTotal characters extracted: {len(text)}")

chunks = split_into_chunks(text)
print(f"Split into {len(chunks)} chunks.\n")

print("Here's the first chunk, so you can see what it looks like:\n")
print(chunks[0])