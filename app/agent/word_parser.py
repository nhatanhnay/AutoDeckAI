from docx import Document
import io

def extract_text_from_word(word_bytes):
    doc = Document(io.BytesIO(word_bytes))
    return "\n".join([para.text for para in doc.paragraphs])