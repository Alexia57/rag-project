from langchain_community.document_loaders import PyPDFLoader

def test_pdf_loading(pdf_path: str):
    """
    Function to test loading and extracting text from a PDF file.

    Args:
        pdf_path (str): The path to the PDF file.
    
    Returns:
        str: Extracted text from the PDF.
    """
    try:
        print(f"🔄 Loading PDF file: {pdf_path}")
        loader = PyPDFLoader(pdf_path)
        documents = loader.load()

        # Check if any content was loaded
        if not documents:
            raise ValueError("⚠️ No text was extracted from the PDF. Check the file content.")

        # Concatenate the content from all loaded documents
        text = "\n\n".join([doc.page_content for doc in documents])
        print("✅ Text successfully extracted!")
        return text

    except FileNotFoundError:
        print("❌ Error: PDF file not found.")
        return None
    except Exception as e:
        print(f"❌ An error occurred: {e}")
        return None


# Example usage
pdf_path = "../gravite.pdf"  # Replace with your PDF file path
extracted_text = test_pdf_loading(pdf_path)

if extracted_text:
    print("💬 Extracted content:")
    print(extracted_text[:500])  # Display the first 500 characters
else:
    print("⚠️ Unable to extract content.")
