docker_compose([
  "./docker-compose-data.yml",
  "./docker-compose-app.yml"
])

dc_resource("weaviate",   labels=["data"])
dc_resource("app",        labels=["app"])
