# Anchor
Personal Project | Creating a personal recommendation engine for the internet with [Louis](https://www.linkedin.com/in/lhorrell/).

### The Idea
**Challenge:** In the digital age, distractions are a click away. We often struggle with online distractions, leading us to website blockers - my favourite it [Prod](https://chromewebstore.google.com/detail/prod-%E2%80%94-block-distractions/cpelgckpifnonijeenjbaglajimalpcl). But what if we could do better? The internet is rich with knowledge-enhancing content, yet it's challenging to find without knowing exactly what you're searching for.

**Solution:** We're developing a personal content recommendation engine. Unlike typical algorithms that lead users astray, ours aims to enrich knowledge, focusing on the specific areas we would like to know more about. 

### Design 
To start, we established some design principles: 
- Simple and functional
- Local and private

Since we're building a private recommendation engine for one, this is mostly going to be a data problem. 

We need: 
- [x] Store or reference articles / websites that might be of interest
- [x] Identify similar articles
- [ ] Create a recommendation engine based on similar articles and how new they are
	- [ ] Clear old articles from database?
	- [ ] Adjust vector database based on user? or layer a similar NN over the top for recommendations - assess choices
	- [ ] Adjust prompt vector as part of recommendation?
### Build

Currently, we have a docker image for weaviate and an app that scrapes new articles and adds them to the database. We can query the database, since all the data is saved as embedding with ada-002 OpenAI embeddings model. 

Next: recommendations! 

