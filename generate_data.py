# import pandas as pd

# # Read only the first 100 rows
# df = pd.read_csv("application/data/user_reviews_big.csv", nrows=100)

# # Save back to CSV
# df.to_csv("application/data/user_reviews.csv", index=False)

import numpy as np
import random

# Open file and write header
with open("application/data/user_reviews.csv", "w") as f:
    f.write("user_id,product_id,rating,review\n")

# Define products and users
product_ids = [f"P{i}" for i in range(1, 100)]
user_ids = [f"U{i}" for i in range(1, 100)]
reviews = [
    "Good product",
    "Bad!",
    "Excellent quality, very satisfied",
    "Terrible experience, would not recommend",
    "Decent value for the price",
    "Fast shipping and well packaged",
    "Poor customer service",
    "Amazing, exceeded my expectations",
    "Not worth the money",
    "Works fine but could be better"
]

# Generate 100k interactions
with open("application/data/user_reviews.csv", "a") as f:
    for i in range(100):
        product = product_ids[(np.random.zipf(2) - 1) % len(product_ids)]
        user = user_ids[(np.random.zipf(2) - 1) % len(user_ids)]

        rating = random.randint(1, 5)
        review = random.choices(reviews)

        f.write(f"{user},{product},{rating},{review[0]}\n")


categories = [
    "Electronics",
    "Books",
    "Clothing",
    "Home & Kitchen",
    "Sports & Outdoors",
    "Health & Personal Care",
    "Toys & Games",
    "Beauty & Cosmetics",
    "Automotive",
    "Grocery & Food"
]
with open("application/data/product_catalog.csv", "w") as f:
    f.write("product_id,category,price\n")

for _ in range(100):
    category = f"{np.random.choice(categories)}"
    price = random.randint(5, 500)
    product = product_ids[(np.random.zipf(2) - 1) % len(product_ids)]

    with open("application/data/product_catalog.csv", "a") as f:
        f.write(f"{product},{category},{price}\n")


with open("application/data/user_interactions.csv", "w") as f:
    f.write("user_id,product_id,interaction,timestamp\n")

interactions= ["click", "view", "purchase"]
for _ in range(100):
    interaction = random.choices(interactions)
    timestamp = 1609459200 + _ * 60
    product = product_ids[(np.random.zipf(2) - 1) % len(product_ids)]
    user = user_ids[(np.random.zipf(2) - 1) % len(user_ids)]
    with open("application/data/user_interactions.csv", "a") as f:
        f.write(f"{user},{product},{interaction[0]},{timestamp}\n")