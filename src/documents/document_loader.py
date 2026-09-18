import pymupdf

def load_pdf(file_path):
    """
    Extract text from every page of a PDF.
    """

    document = pymupdf.open(file_path)
    pages = []

    for page_number, page in enumerate(document, start=1):
        text = page.get_text()
        pages.append({
            "page_number": page_number,
            "text": text
        })
    document.close()

    return pages