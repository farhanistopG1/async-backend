"""
knowledge_ingest.exceptions

Custom exceptions used throughout the Knowledge Organism.

Every stage of the ingestion pipeline raises its own exception,
making debugging much easier.
"""


class KnowledgeIngestError(Exception):
    """Base exception for the package."""

    pass


class LoaderError(KnowledgeIngestError):
    """Raised when a document cannot be loaded."""

    pass


class ChunkingError(KnowledgeIngestError):
    """Raised when chunking fails."""

    pass


class EmbedError(KnowledgeIngestError):
    """Raised when embedding generation fails."""

    pass