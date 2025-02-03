from PyPDF2 import PdfReader

def test_pdf_loading(pdf_path: str):
    try:
        print(f"🔄 Loading PDF: {pdf_path}")
        reader = PdfReader(pdf_path)
        for page_num, page in enumerate(reader.pages[:3]):  # Affiche les 3 premières pages
            print(f"Page {page_num + 1}:")
            print(page.extract_text())  # Limite à 500 caractères par page
        print("✅ PDF loaded and previewed successfully!")
    except Exception as e:
        print(f"❌ Failed to load PDF: {e}")

# Test with a sample PDF
test_pdf_loading("../gravite.pdf")
