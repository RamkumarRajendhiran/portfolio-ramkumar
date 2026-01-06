import pdfplumber

pdf_path = r'c:\Users\sivap\Downloads\portfolio1\portfolio-Ramkumar\RAMKUMAR-RAJENDHIRAN resume.pdf'
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        print(page.extract_text())
