from weaviate import Client, AuthClientPassword
# Connect to Weaviate
client = Client("http://localhost:8080")

# Prepare your data object
schema = {
    "classes": [
        {
            "class": "WebPage",
            "description": "A class to store information about web pages",
            "properties": [
                {
                    "name": "url",
                    "dataType": ["string"],
                    "description": "The URL of the web page"
                },
                {
                    "name": "title",
                    "dataType": ["string"],
                    "description": "The title of the web page"
                },
                {
                    "name": "content",
                    "dataType": ["text"],
                    "description": "The content or body of the web page"
                }
            ]
        }
    ]
}

client.schema.create(schema)