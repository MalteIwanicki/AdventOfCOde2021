import pandas as pd

df = pd.read_csv("2/input.csv", " ", names=["order", "value"])

x = 0
y = 0
aim = 0

for index, row in df.iterrows():
    if row["order"] == "forward":
        x += row["value"]
        y += aim * row["value"]
    if row["order"] == "up":
        aim -= row["value"]
    if row["order"] == "down":
        aim += row["value"]

print(f"{x*y}")
