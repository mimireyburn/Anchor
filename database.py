from weaviate import Client, AuthClientPassword
# Connect to Weaviate
from scrape import get_data
from embeddings import get_embedding
import json

client = Client("http://localhost:8080")

def create_schema(client):
    # Define schema
    schema = {
        "classes": [{
            "class": "Article",
            "properties": [
                {"name": "url", "dataType": ["string"]},
                {"name": "title", "dataType": ["string"]},
                {"name": "content", "dataType": ["string"]},
                {"name": "embedding", "dataType": ["number"], "indexInverted": False}
            ]
        }]
    }
    client.schema.create(schema)


def add_data(data):
    """ 
    Add data to Weaviate
    data : {
        "url": "https://example.com/",
        "title": "Example Page One",
        "content": "Article content", 
        "embedding": [0.1, 0.2, 0.3, ...]
    }
    """
    uuid = client.data_object.create(class_name="Article", data_object=data) 
    print("UUID:", uuid)


def query_similar_articles(embedding):
    return client.query.get("Article", ["url", "title"]).with_near_vector(embedding).do()


# create_schema(client)   

urls = ['https://www.theguardian.com', 'https://www.bbc.co.uk/news', 'https://www.theverge.com', 'https://news.ycombinator.com', 'https://www.technologyreview.com']
# get_data(urls)

i=0

with open('articles.json') as file:
    data = file.read()
    articles = json.loads(data)

while i < 5: 
    for article in articles:
        print(article)
        if article['content'] != None:
            article['embedding'] = get_embedding(article['content'])
            print(article['embedding'])
            print(article.keys())
            add_data(article)
            i += 1
        else: 
            print("No content")
            continue

