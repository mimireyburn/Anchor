import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

articles_df = pd.read_json("dummy-articles-with-embeddings.json")

matrix = np.vstack(articles_df.hl_embedding.values)
n_clusters = 3

kmeans = KMeans(n_clusters=n_clusters, init="k-means++", random_state=42)
kmeans.fit(matrix)

articles_df["cluster"] = kmeans.labels_

# select columns A and B
df_hl_cluster = articles_df[["headline", "cluster"]]
print(df_hl_cluster)
