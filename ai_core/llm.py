from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

def get_llm():
    return ChatGroq(
        model="openai/gpt-oss-120b",
        temperature=0.2,
        api_key=os.getenv("GROQ_API_KEY")
    )
