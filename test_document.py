from src.documents.document_loader import load_pdf
from src.documents.text_cleaner import TextCleaner
from src.documents.chunker import TextChunker
from src.documents.metadata import ChunkMetadata
from src.knowledge_base.database import insert_chunk

PDF_PATH = "data/safety_manual.pdf"

if __name__ == "__main__":
    pages = load_pdf(PDF_PATH)
    for page in pages:
        cleaned_text = TextCleaner.clean_text(
            page["text"]
        )
        chunks = TextChunker.create_chunks(
            cleaned_text
        )
        for chunk_number, chunk in enumerate(
            chunks,
            start=1
        ):
            chunk_id = (
                f"page_{page['page_number']}_chunk_{chunk_number}"
            )
            metadata = ChunkMetadata(
                filename="safety_manual.pdf",
                file_type="PDF",
                document_type="Safety Manual",
                page_number=page["page_number"],
                chunk_id=chunk_id
            )
            insert_chunk(
                filename=metadata.filename,
                file_type=metadata.file_type,
                document_type=metadata.document_type,
                page_number=metadata.page_number,
                chunk_id=metadata.chunk_id,
                content=chunk
            )