import pandas as pd
from faker import Faker
import random

fake = Faker()

data = []

for i in range(1000):
    data.append({
        "customer_name": fake.name(),
        "phone": fake.phone_number(),
        "city": fake.city()
    })

df = pd.DataFrame(data)

df.to_csv("customers.csv", index=False)

print("Dataset Generated")