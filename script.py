import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random

df = pd.read_csv("dataset.csv")

df.columns = ["ID", "Entity", "Sentiment", "Text"]

df.dropna(subset=["Entity", "Sentiment"], inplace=True)

df["Sentiment"] = df["Sentiment"].str.capitalize()

unique_entities = df["Entity"].dropna().unique().tolist()
selected_entities = random.sample(unique_entities, min(10, len(unique_entities)))

filtered_df = df[df["Entity"].isin(selected_entities)]

sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))

sns.countplot(
    x="Entity",
    hue="Sentiment",
    data=filtered_df,
    order=selected_entities,
    palette="pastel"
)

plt.title("Sentiment Distribution for 10 Random Hot Topics")
plt.xlabel("Topic")
plt.ylabel("Tweet Count")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("hot_topics_sentiment_distribution.png")
plt.show()
