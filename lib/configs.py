import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PALM_API_KEY = os.getenv("PALM_API_KEY")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
