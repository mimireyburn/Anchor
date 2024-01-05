import weaviate
import weaviate.classes as wvc
import os 
from dotenv import load_dotenv

load_dotenv()

# As of November 2023, we are working towards making all WCS instances compatible with the new API introduced in the v4 Python client.
# Accordingly, we show you how to connect to a local instance of Weaviate.
# Here, authentication is switched off, which is why you do not need to provide the Weaviate API key.
client = weaviate.connect_to_local(
    port=8080,
    grpc_port=50051,
    headers={
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]  # Replace with your inference API key
    }
)

articles = client.collections.get("News")

response = articles.query.near_text(
    query="AI Apocalpyse",
    limit=1
)

print(response.objects[0].properties["title"], response.objects[0].properties["url"])  # Inspect the first object