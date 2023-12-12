from weaviate import Client, AuthClientPassword
# Connect to Weaviate
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
