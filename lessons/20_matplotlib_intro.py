import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "name": ["Rafi", "Mim", "Anik", "Tania", "Sumon", "Nila"],
    "dept": ["IT", "HR", "IT", "Sales", "HR", "IT"],
    "salary": [50000, 60000, 60000, 80000, 52000, 70000],
})

avg = df.groupby("dept")["salary"].mean()

plt.figure(figsize=(6, 4))
plt.bar(avg.index, avg.values)
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.savefig("avg_salary.png")
plt.show()