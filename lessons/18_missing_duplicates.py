import pandas as pd

df = pd.read_csv("staff.csv")

print(df.isna().sum())
print(df.dropna())

df["age"] = df["age"].fillna(df["age"].mean())
df["salary"] = df["salary"].fillna(df["salary"].median())
print(df)

df = pd.concat([df, df.iloc[[0]]], ignore_index=True)
print(df.duplicated().sum())

df = df.drop_duplicates()
print(len(df))