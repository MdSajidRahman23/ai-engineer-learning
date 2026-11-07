import pandas as pd

data = {
    "name": ["Rafi", "Mim", "Anik", "Tania", "Sumon"],
    "age": [25, 32, None, 40, 29],
    "salary": [50000, 60000, 55000, None, 52000],
}

df = pd.DataFrame(data)
df.to_csv("staff.csv", index=False)

df2 = pd.read_csv("staff.csv")

print(df2.head(3))
df2.info()
print(df2.isna().sum())
print(df2.describe())
