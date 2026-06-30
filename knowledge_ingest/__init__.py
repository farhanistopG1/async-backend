"""
Knowledge Ingest

A lightweight knowledge ingestion SDK.

Public API:

    from knowledge_ingest import KnowledgeOrganism

    organism = KnowledgeOrganism()

    chunks = organism.ingest("Knowledge_base/capsule.md")

    embedded = organism.embed(chunks)
"""

from .organism import KnowledgeOrganism

__version__ = "0.1.0"

__all__ = [
    "KnowledgeOrganism",
]