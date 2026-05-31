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

async def brain(prompt):
    response = await deepseek_client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role": "user", "content": prompt
            }
        ]
    )
    return response.choices[0].message.content