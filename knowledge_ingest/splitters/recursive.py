"""
knowledge_ingest.splitters.recursive

Recursive text splitter.

Responsibility
--------------
Raw Document Text
        ↓
KnowledgeChunk[]

Uses LangChain's RecursiveCharacterTextSplitter internally,
but exposes only our own KnowledgeChunk objects.
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter

from knowledge_ingest.exceptions import ChunkingError
from knowledge_ingest.models import KnowledgeChunk


class RecursiveSplitter:
    """
    Converts a document into KnowledgeChunk objects.
    """

    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ) -> None:

        self._splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

    def split(
        self,
        text: str,
        source: str,
    ) -> list[KnowledgeChunk]:
        """
        Parameters
        ----------
        text
            Raw document text.

        source
            Original filename.

        Returns
        -------
        list[KnowledgeChunk]
        """

        try:

            pieces = self._splitter.split_text(text)

            chunks = []

            total_chunks = len(pieces)

            for index, piece in enumerate(pieces, start=1):

                chunks.append(
                    KnowledgeChunk(
                        chunk_id=index,
                        source=source,
                        text=piece,
                        metadata={
                            "total_chunks": total_chunks,
                            "splitter": "recursive",
                        },
                    )
                )

            return chunks

        except Exception as e:
            raise ChunkingError(
                f"Chunking failed: {e}"
            ) from e