from openai import AsyncOpenAI
from dotenv import load_dotenv
import os

load_dotenv(override=True)
api_key = os.getenv("DEEPSEEK_API_KEY")
if not api_key:
    raise ValueError("Deepseek API-KEY not found")

deepseek_client = AsyncOpenAI(
    api_key = api_key,
    base_url="https://api.deepseek.com/v1"
)

async def brain(prompt, context):
    response = await deepseek_client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role": "user", "content": prompt
            },
            {
                "role": "system", "content": f"""You can have additinal reference to answer the user question more propely using the context i will provide you pleae note that this is the user memory which is stored.
                
                context = {context}"""
            }
        ]
    )
    return response.choices[0].message.content