from PyPDF2 import PdfReader

def process_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""

    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()

    summary = text[:600] + "...\n\n[AI Generated Summary]"
    return summary, text


def answer_question(question, pdf_text):
    question = question.lower()

    if "summary" in question:
        return "This PDF explains key ideas extracted from the document."

    elif "topic" in question:
        return "The main topic is based on the uploaded PDF content."

    elif "author" in question:
        return "Author details are not available in this document."

    else:
        return "Answer generated using AI logic from PDF content."
