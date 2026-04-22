from ucimlrepo import fetch_ucirepo
import pandas as pd
import os

os.makedirs("data", exist_ok=True)

print("Downloading dataset...")
drug_reviews = fetch_ucirepo(id=462)
df = drug_reviews.data.features

df.to_csv("data/processed_drug_reviews.csv", index=False)
print("Dataset saved to data/processed_drug_reviews.csv")