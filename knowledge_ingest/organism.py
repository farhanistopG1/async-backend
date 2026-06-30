"""
knowledge_ingest.organism

Public entrypoint of the Knowledge Organism.

Pipeline

Document
    ↓
MarkdownLoader
    ↓
Raw Text
    ↓
RecursiveSplitter
    ↓
KnowledgeChunk[]
    ↓
GeminiEmbedder
    ↓
EmbeddedKnowledgeChunk[]
"""

import os

from dotenv import load_dotenv


from knowledge_ingest.loaders.markdown import MarkdownLoader
from knowledge_ingest.models import (
    EmbeddedKnowledgeChunk,
    KnowledgeChunk,
)
from knowledge_ingest.splitters.recursive import RecursiveSplitter


load_dotenv()


class KnowledgeOrganism:
    """
    Public interface of the SDK.
    """

    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ):

        self.loader = MarkdownLoader()

        self.splitter = RecursiveSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

    def ingest(
        self,
        path: str,
    ) -> list[KnowledgeChunk]:
        """
        Load a document and convert it into chunks.
        """

        text, source = self.loader.load(path)

        chunks = self.splitter.split(
            text=text,
            source=source,
        )

        return chunks

    def embed(
    self,
    chunks: list[KnowledgeChunk],
    api_key: str | None = None,
) -> list[EmbeddedKnowledgeChunk]:
        from knowledge_ingest.embedders.openrouter import OpenRouterEmbedder
        api_key = api_key or os.getenv("OPENROUTER_API_KEY")
        
        embedder = OpenRouterEmbedder(api_key)

        return embedder.embed(chunks)
    
    def embed_query(
    self,
    question: str,
    api_key: str | None = None,
) -> list[float]:
        from knowledge_ingest.embedders.openrouter import OpenRouterEmbedder

        api_key = api_key or os.getenv("OPENROUTER_API_KEY")

        embedder = OpenRouterEmbedder(api_key)
        
        return embedder.embed_query(question)

        


   

    
    
  

   


        

   

    


    

    
    