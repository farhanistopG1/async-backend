"""
knowledge_ingest.models

Core data models used throughout the Knowledge Organism.

Every stage transforms one model into another.

Document
    ↓
KnowledgeChunk
    ↓
EmbeddedKnowledgeChunk
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class KnowledgeChunk:
    """
    Represents one chunk of human-readable knowledge.

    Produced by:
        Loader -> Splitter
    """

    chunk_id: int
    source: str
    text: str
    metadata: dict = field(default_factory=dict)


@dataclass(slots=True)
class EmbeddedKnowledgeChunk(KnowledgeChunk):
    """
    Represents a KnowledgeChunk after embedding.

    Produced by:
        GeminiEmbedder
    """

    embedding: list[float] = field(default_factory=list)