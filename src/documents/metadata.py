from pydantic import BaseModel
from typing import Optional


class ChunkMetadata(BaseModel):
    filename: str
    file_type: str
    document_type: str
    page_number: int
    chunk_id: str
    uploaded_by: Optional[str] = None