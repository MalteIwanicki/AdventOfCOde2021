import pandas as pd

df = pd.read_csv("day2/input.csv", " ", names=["order", "value"])

x = 0
y = 0
forwards = df.loc[df["order"] == "forward", "value"].sum()
downs = df.loc[df["order"] == "down", "value"].sum()
ups = df.loc[df["order"] == "up", "value"].sum()
x += forwards
y += downs - ups
print(f"{x*y}")
