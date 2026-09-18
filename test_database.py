from src.knowledge_base.database import test_connection
from src.knowledge_base.database import insert_chunk


if __name__ == "__main__":

    test_connection()

    insert_chunk(
        filename="safety_manual.pdf",
        file_type="PDF",
        document_type="Safety Manual",
        page_number=1,
        chunk_id="chunk_test_01",
        content="Safety Helmet Mandatory in production and construction areas."
    )