import psycopg 
import json 
from pgvector.psycopg import register_vector
from pgvector import Vector

connection = psycopg.connect(
    dbname="my_capsules",
    user="farhanahmedmudgal"
)

register_vector(connection)


cursor = connection.cursor()

def create_table():
    cursor.execute("""
CREATE TABLE IF NOT EXISTS knowledge_chunks (
                   id SERIAL PRIMARY KEY,
                   chunk_id INTEGER NOT NULL,
                   source TEXT NOT NULL,
                   text TEXT NOT NULL,
                   metadata JSONB NOT NULL DEFAULT '{}',
                   embedding VECTOR(1536) NOT NULL );   
""")
    connection.commit()


def store(chunk):
    cursor.execute("""
INSERT INTO knowledge_chunks 
                   (
                   chunk_id,
                   source,
                   text,
                   metadata,
                   embedding
                   )
                   VALUES 
                   (
                   %s,
                   %s,
                   %s,
                   %s,
                   %s
                   )
""", (
    chunk.chunk_id,
    chunk.source,
    chunk.text,
    json.dumps(chunk.metadata),
    chunk.embedding
))
    connection.commit()


def search(query_embedding):

    try:

        cursor.execute("""
            SELECT
                text,
                metadata
            FROM knowledge_chunks
            ORDER BY embedding <=> %s
            LIMIT 5
        """, (Vector(query_embedding),)
        )

        return cursor.fetchall()

    except Exception as e:

        connection.rollback()

        raise
    
    