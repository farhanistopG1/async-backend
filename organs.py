from brain import brain 
import logging

logging.basicConfig(
    filename="system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
cache_query = {}
cache_review = {}
bad_customer_keywords = [
    "broken",
    "cheap",
    "useless",
    "defective",
    "garbage",
    "trash",
    "terrible",
    "horrible",
    "faulty",
    "flimsy",
    "stopped",
    "fake",
    "disappointed",
    "late",
    "missing",
    "damaged",
    "never",
    "delayed",
    "empty",
    "wrong",
    "lost",
    "rude",
    "ignored",
    "unhelpful",
    "refused",
    "bot",
    "automated",
    "ghosted",
    "transfer",
    "clueless",
    "hours",
    "scam",
    "rip-off",
    "refund",
    "charged",
    "hidden",
    "stole",
    "cancel",
    "overpriced",
    "fees",
    "worst",
    "waste",
    "regret",
    "error",
    "broken-link",
    "confusing",
    "misleading",
    "avoid",
    "unacceptable",
    "frustrated"
]

bad_restaurant_keywords = [
    "cold",
    "raw",
    "burnt",
    "overcooked",
    "undercooked",
    "bland",
    "tasteless",
    "salty",
    "greasy",
    "oily",
    "dry",
    "stale",
    "soggy",
    "spoiled",
    "sour",
    "bitter",
    "rubbery",
    "hair",
    "bug",
    "fly",
    "dirty",
    "filthy",
    "unclean",
    "smelly",
    "stink",
    "sick",
    "nausea",
    "poisoning",
    "rude",
    "slow",
    "ignored",
    "forgotten",
    "waiting",
    "hours",
    "inattentive",
    "wrong",
    "overpriced",
    "rip-off",
    "scam",
    "disgusting",
    "gross",
    "vile",
    "awful",
    "terrible",
    "horrible",
    "worst",
    "waste",
    "disappointed",
    "avoid",
    "never-again"
]
#_____Customer Support Reply Generator_____

def process_customer_query(query):
    cleanup = query.strip().lower()
    return any(keyword in cleanup for keyword in bad_customer_keywords)
            

def build_prompt(query):
    if process_customer_query(query):
            logging.info(f"negative query detected: {query}")
            return f"""
You are an Ai assistant for customer support.
You have an amazing ability to understant customer queries and generate short and helpful replies which acknowledge the customer's feelings and provide a soltion to their problem

user query: {query}
   
"""
    logging.info(f"neutral/positive query detected: {query}")
    return f"""
    You are an Ai assistant for customer support.
You have an amazing ability to understant customer queries and generate short and helpful replies which acknowledge the customer's feelings and provide a soltion to their problem

user query: {query}"""


        
    
async def generate_reply(query):
    #try block 
    try:
        logging.info(f"starting reply generation for query") 
        if query in cache_query:
            logging.info(f"cache hit for query: {query}")
            return {
            "from": "AI Assistnat🤖",
            "reply": cache_query[query]
        }
        logging.info(f"cache miss for query: {query}")
        #retry block 
        for attempts in range(3):
            try:
                logging.info(f"sending query to brain, attempt {attempts + 1} for query:{query}")
                cache_query[query] = await brain(build_prompt(query))
                logging.info(f"successfully received reply from brain for query: {query}") 
                logging.info(f"reply generation done for query: {query}")
                return {
                    "from": "AI Assistant🤖",
                    "reply": cache_query[query]
                }       
            except Exception as e:
                logging.error(f"Attempt {attempts + 1} failed : {e}")
        return {
            "error": "Failed to generate a reply after multiple attempts."
        }
    except Exception as e:
        logging.error(f"Error in GenerateReply: {e}")
        return {
            "error": str(e)
        }  
    



#_________Restaurant Review Analyzer______

def process_review(review):
    cleanup = review.strip().lower()
    return any(keyword in cleanup for keyword in bad_restaurant_keywords)

def build_review_prompt(review):
    if process_review(review):
            logging.info(f"negative review detected: {review}")
            return f"""
you are an Ai assistant for restaurant review analysis.

your main task is to analyze the restaurant review and determine if the review is positive or negative. IF the review is negative you will provide a short summary for the Restaurant General Manager to understand the main issues and key point which will help resolve the same in 1 line.

user review: {review}
"""
    logging.info(f"neutral/positive review detected: {review}")
    return f"""
    you are an Ai assistant for restaurant review analysis. If the review is negative you will provide a short summary for the Restaurant General Manager to understand the main issues and key point which will help resolve the same in 1 line.
    
    user review : {review}
    """    
    
    
async def analyze_review(review):
    try:
        logging.info(f"starting review analysis for review")
        if review in cache_review:
            logging.info(f"cache hit for review: {review}")
            return {
            "from": "AI Assistant🤖",
            "analysis": cache_review[review]
        }
        logging.info(f"cache miss for review: {review}")
        #retry block
        for attempts in range(3):
            try:
                logging.info(f"sending review to brain, attempt {attempts + 1} for review:{review}")
                cache_review[review] = await brain(build_review_prompt(review))
                logging.info(f"successfully received analysis from brain for review: {review}") 
                logging.info(f"Analysis done for review: {review}")
                return {"from" : "AI Assistant🤖",
                        "analysis" : cache_review[review]
                        }        
            except Exception as e:
                logging.error(f"Attempt {attempts + 1} failed : {e}")
        return {
            "error" : "Failed to analyze the review after multiple attempts."
        }
    except Exception as e:
        logging.error(f"Error in AnalyzeReview: {e}")
        return {
            "error": str(e)
        }
        
    
        
        
    
    
    
        
    
    




    
