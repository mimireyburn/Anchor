import requests
import json
import os

import weaviate
import weaviate.classes as wvc
import os
from dotenv import load_dotenv

load_dotenv()

client = weaviate.connect_to_local(
    port=8080,
    grpc_port=50051,
    headers={
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]  # Replace with your inference API key
    }
)

def create_schema(client):
    articles = client.collections.create(
        name="News",
        vectorizer_config=wvc.Configure.Vectorizer.text2vec_openai(),  # If set to "none" you must always provide vectors yourself. Could be any other "text2vec-*" also.
        generative_config=wvc.Configure.Generative.openai()  # Ensure the `generative-openai` module is used for generative queries
    )

def add_data(client, article_objs):
    articles = client.collections.get("News")
    articles.data.insert_many(articles_objs)


urls = ['https://www.theguardian.com', 'https://www.bbc.co.uk/news', 'https://www.theverge.com', 'https://news.ycombinator.com', 'https://www.technologyreview.com']

with open('articles.json') as file:
    data = json.load(file)

count = 0
articles_objs = list()
for article in data:
    if count <= 200:
        if article['content'] != None:
            articles_objs.append(article)
            # print(article)
            count += 1
            print(count)
        else: 
            print("No content")
            continue

# create_schema(client)
add_data(client, articles_objs)
