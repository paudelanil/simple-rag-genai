from pypdf import PdfReader

reader = PdfReader("../data/raw")
text = ""
for page in reader.pages:
    text += page.extract_text() or ""

print(f"Extracted text length: {len(text)}")