import json
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load env variables
load_dotenv()

# Init OpenAI client
client = OpenAI()


# Function to retrieve embeddings from OpenAI API
def get_embedding(text, model="text-embedding-ada-002"):
    text = text.replace("\n", " ")
    return client.embeddings.create(input=[text], model=model).data[0].embedding


# Load articles
with open("dummy-articles.json") as file:
    data = file.read()
    articles = json.loads(data)

# Add headline embedding for each article
for a in articles:
    a["hl_embedding"] = get_embedding(a["headline"])
    a["content_embedding"] = get_embedding(a["article-content"])

# Save output to JSON (prevent too much API use)
with open("dummy-articles-with-embeddings.json", "w") as outfile:
    json.dump(articles, outfile)
