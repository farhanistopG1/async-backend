"""
knowledge_ingest.embedders.openrouter

Embeds KnowledgeChunks using OpenRouter's embedding API.

Responsibility
--------------
KnowledgeChunk[]
        ↓
EmbeddedKnowledgeChunk[]
"""

from openai import OpenAI

from knowledge_ingest.exceptions import EmbedError
from knowledge_ingest.models import (
    EmbeddedKnowledgeChunk,
    KnowledgeChunk,
)


class OpenRouterEmbedder:

    MODEL = "openai/text-embedding-3-small"

    def __init__(self, api_key: str):

        if not api_key:
            raise EmbedError(
                "OPENROUTER_API_KEY is required."
            )

        self.client = OpenAI(
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1",
        )

    def embed(
        self,
        chunks: list[KnowledgeChunk],
    ) -> list[EmbeddedKnowledgeChunk]:

        embedded_chunks = []

        for chunk in chunks:

            try:

                response = self.client.embeddings.create(
                    model=self.MODEL,
                    input=chunk.text,
                )

                embedding = response.data[0].embedding

                embedded_chunks.append(
                    EmbeddedKnowledgeChunk(
                        chunk_id=chunk.chunk_id,
                        source=chunk.source,
                        text=chunk.text,
                        metadata=chunk.metadata,
                        embedding=embedding,
                    )
                )

            except Exception as e:

                raise EmbedError(
                    f"Failed to embed chunk {chunk.chunk_id}: {e}"
                ) from e

        return embedded_chunks
    
    def embed_query(
    self,
    question: str,
) -> list[float]:
        
        try:
            response = self.client.embeddings.create(
            model=self.MODEL,
            input=question,
        )
            return response.data[0].embedding
        
        except Exception as e:
            raise EmbedError(
            f"Failed to embed question: {e}"
        ) from e
    

   


        
    
    




    


        