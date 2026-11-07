import pandas as pd

data = {"city": ["Dhaka", "Savar"], "temp": [30, 28]}
df = pd.DataFrame(data)
print(df)

print(df["city"])
print(df["temp"])

print(df["temp"].mean())
print(df["temp"].max())

print(df[df["temp"] > 29])


df["temp_f"] = df["temp"] * 9 / 5 + 32
print(df)


print(df.sort_values("temp"))
print(df.sort_values("temp", ascending=False))