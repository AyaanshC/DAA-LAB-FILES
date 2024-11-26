import numpy as np 
import pandas as pd

x = pd.read_csv("courier_items_dataset_3.csv")

x["Ratio"] = x["Value"] / (x["Weight"] * x["Shelf_Life"])
x.sort_values(by="Ratio", ascending=False, inplace=True)

max_weight = 200
weight = 0
items = []
total_value = 0
i = 0

while weight < max_weight and i < len(x):
    item_weight = x.iloc[i]["Weight"]
    item_value = x.iloc[i]["Value"]
    
    if weight + item_weight <= max_weight:
        # Choose the whole item
        weight += item_weight
        total_value += item_value
        items.append((item_value, item_weight))  
    else:
        # Choose the fractional part of the item
        fraction = (max_weight - weight) / item_weight
        weight += item_weight * fraction
        total_value += item_value * fraction
        items.append((item_value * fraction, item_weight * fraction))
        break 
    i += 1

# Print Data
for item_value, item_weight in items:
    print(f"Item with value {item_value} and weight {item_weight}")

print(f"The total value of the knapsack is: {total_value}")
