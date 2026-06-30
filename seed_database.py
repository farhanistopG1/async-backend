from knowledge_ingest import KnowledgeOrganism
from database import store

organism = KnowledgeOrganism()


chunks = organism.ingest("Knowledge_base/capsule.md")

embedded_chunks = organism.embed(chunks)

for chunk in embedded_chunks:
    store(chunk)
    


