import PyPDF2
from services import generate_text


def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text


def extract_text_from_multiple_pdfs(files):
    full_text = ""

    for file in files:
        full_text += extract_text_from_pdf(file) + "\n"

    return full_text[:8000]   # limit


def analyze_pdf(files):
    text = extract_text_from_multiple_pdfs(files)

    return generate_text(f"""
    Analyze this content:

    {text}

    Give:
    1. Summary
    2. Key Points
    3. 5 Quiz Questions with answers
    """)


def ask_pdf_question(files, question):
    text = extract_text_from_multiple_pdfs(files)

    return generate_text(f"""
    Answer this question based ONLY on the PDF content:

    {text}

    Question: {question}
    """)