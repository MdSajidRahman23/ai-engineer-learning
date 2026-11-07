import pandas as pd

data = {
    "name": ["Rafi", "Mim", "Anik", "Tania"],
    "age": [25, 32, 28, 40],
    "salary": [50000, 60000, 55000, 80000],
}

df = pd.DataFrame(data)

print(df)
print(df["age"])
print(df[df["age"] > 27])
print(df["salary"].mean())