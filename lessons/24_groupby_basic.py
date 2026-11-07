import pandas as pd

df = pd.DataFrame({
    "city": ["Dhaka", "Savar", "Dhaka", "Savar"],
    "temp": [30, 28, 34, 26],
})

print(df.groupby("city")["temp"].mean())


print(df.groupby("city")["temp"].count())
print(df.groupby("city")["temp"].max())