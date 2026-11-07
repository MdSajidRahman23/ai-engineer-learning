import pandas as pd

df = pd.DataFrame({
    "name": ["Rafi", "Mim", "Anik", "Tania", "Sumon", "Nila"],
    "dept": ["IT", "HR", "IT", "Sales", "HR", "IT"],
    "salary": [50000, 60000, 60000, 80000, 52000, 70000],
})

print(df.groupby("dept")["salary"].mean())
print(df.groupby("dept")["salary"].count())
print(df.sort_values("salary", ascending=False))
print(df.sort_values(["dept", "salary"], ascending=[True, False]).head(3))