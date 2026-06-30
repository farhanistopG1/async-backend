# knowledge-ingest

Production-ready Knowledge Ingestion SDK for AI systems.

**Document → Chunks → Embeddings → pgvector. In one call.**

Built for AI automation backends that follow the Two-Organism Architecture.
Designed by Farhan Ahmed Mudgal · Nova Automate · 2026.

---

## Install

```bash
pip install knowledge-ingest
```

## Quickstart

```python
from knowledge_ingest import KnowledgeOrganism

organism = KnowledgeOrganism(
    api_key="your-gemini-key",
    db_url="postgresql://user:pass@localhost/dbname",
)

# Full pipeline — one call
organism.run("capsule.md")
```

## Step-by-step

```python
# 1. Load + chunk
chunks = organism.ingest("sop.md")           # List[KnowledgeChunk]

# 2. Embed
embedded = organism.embed(chunks)            # List[EmbeddedKnowledgeChunk]

# 3. Write to pgvector
organism.write(embedded)                     # None
```

## Configuration

Constructor arguments take priority over environment variables.

| Argument       | Env Var           | Default              |
|----------------|-------------------|----------------------|
| `chunk_size`   | `KO_CHUNK_SIZE`   | `800`                |
| `chunk_overlap`| `KO_CHUNK_OVERLAP`| `100`                |
| `api_key`      | `GEMINI_API_KEY`  | required             |
| `db_url`       | `DATABASE_URL`    | required             |
| `table_name`   | `KO_TABLE_NAME`   | `knowledge_chunks`   |

## Required Table Schema

This package does **not** create tables. Run this once in your database:

```sql
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE knowledge_chunks (
    id         SERIAL PRIMARY KEY,
    chunk_id   INTEGER     NOT NULL,
    source     TEXT        NOT NULL,
    text       TEXT        NOT NULL,
    metadata   JSONB       NOT NULL DEFAULT '{}',
    embedding  vector(768) NOT NULL
);

CREATE INDEX ON knowledge_chunks
USING hnsw (embedding vector_cosine_ops);
```

## Models

```python
# After ingest()
KnowledgeChunk(
    chunk_id=0,
    source="capsule.md",
    text="...",
    metadata={"position": 0, "total_chunks": 12, "splitter": "recursive"},
)

# After embed()
EmbeddedKnowledgeChunk(
    chunk_id=0,
    source="capsule.md",
    text="...",
    metadata={...},
    embedding=[0.012, -0.034, ...],  # 768 floats — Gemini text-embedding-004
)
```

## Supported Formats

| Version | Format                        |
|---------|-------------------------------|
| v1.0    | Markdown (`.md`, `.markdown`) |
| v1.1    | PDF (planned)                 |
| v1.2    | DOCX (planned)                |
| v1.3    | HTML (planned)                |

## Architecture

The chunking engine, embedder, and writer are all swappable.
Today it uses LangChain's RecursiveCharacterTextSplitter internally.
Tomorrow you can swap in Docling's HybridChunker without changing
your calling code.

```
Document
    -> Loader (MarkdownLoader)
    -> Splitter (RecursiveSplitter)
    -> KnowledgeChunk[]
    -> Embedder (GeminiEmbedder)
    -> EmbeddedKnowledgeChunk[]
    -> Writer (PgVectorWriter)
    -> PostgreSQL + pgvector
```

## Exceptions

```python
from knowledge_ingest import (
    KnowledgeIngestError,  # base — catch all
    LoaderError,           # file not found, unsupported type
    ChunkError,            # splitting failed
    EmbedError,            # API error, missing key
    WriteError,            # database write failed
)
```

## License

MIT
