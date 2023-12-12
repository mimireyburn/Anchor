import weaviate

# Initialize the Weaviate client
client = weaviate.Client("http://localhost:8080")  # Replace with your Weaviate URL if not running locally

# Dummy data
web_pages = [
    {
        "url": "https://example.com/page1",
        "title": "Example Page One",
        "content": "This is the content of the first example page. It contains information about various topics related to Example One."
    },
    {
        "url": "https://example.com/page2",
        "title": "Example Page Two",
        "content": "This is the content of the second example page. It offers insights and information on topics pertaining to Example Two."
    },
    {
        "url": "https://example.com/page3",
        "title": "Example Page Three",
        "content": "This is the content of the third example page. Here, you'll find a variety of resources and discussions related to Example Three."
    }
]

# Adding each web page to Weaviate
for page in web_pages:
    print(page)
    uuid = client.data_object.create(class_name="WebPage", data_object=page)  # UUID is auto-generated if set to None
    print("UUID:", uuid)    
print("Data added to Weaviate successfully!")