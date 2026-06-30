from pydantic import BaseModel
from fastapi import FastAPI
from organs import generate_reply
from organs import analyze_review
from knowledge_ingest import KnowledgeOrganism
from database import search

app = FastAPI()
organism = KnowledgeOrganism()

class CustomerSupportRequest(BaseModel):
    customer_query : str

class RestaurantReviewAnalyzer(BaseModel):
    review : str


@app.post("/customer-support")
async def customer_support(reply : CustomerSupportRequest):
    query_embedding = organism.embed_query(reply.customer_query) 
    retrieved_memory = search(query_embedding)
    return await generate_reply(reply.customer_query, retrieved_memory)
    

@app.post("/restaurant-review-analyzer")
async def review_analyzer(feedback : RestaurantReviewAnalyzer):
    query_embedding = organism.embed_query(feedback.review)
    retrieved_memory = search(query_embedding)
    return await analyze_review(feedback.review, retrieved_memory)


