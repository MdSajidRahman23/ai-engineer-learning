import pandas as pd

df = pd.read_csv("weather.csv")
print(df)
print(df.groupby("city")["temp"].mean())