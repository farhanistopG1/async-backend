from pydantic import BaseModel
from fastapi import FastAPI
from organs import generate_reply
from organs import analyze_review

app = FastAPI()

class CustomerSupportRequest(BaseModel):
    customer_query : str

class RestaurantReviewAnalyzer(BaseModel):
    review : str


@app.post("/customer-support")
async def customer_support(reply : CustomerSupportRequest):
    return await generate_reply(reply.customer_query)

@app.post("/restaurant-review-analyzer")
async def review_analyzer(feedback : RestaurantReviewAnalyzer):
    return await analyze_review(feedback.review)



