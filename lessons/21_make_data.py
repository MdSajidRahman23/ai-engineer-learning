import numpy as np
import pandas as pd

np.random.seed(7)
n = 40

df = pd.DataFrame({
    "student_id": np.arange(1, n + 1),
    "dept": np.random.choice(["CSE", "EEE", "BBA", "English"], n),
    "study_hours": np.random.randint(1, 9, n).astype(float),
    "marks": np.random.randint(35, 100, n).astype(float),
})

df.loc[[3, 11, 25], "marks"] = np.nan
df.loc[[7, 19], "study_hours"] = np.nan
df = pd.concat([df, df.iloc[[5]]], ignore_index=True)

df.to_csv("students.csv", index=False)
print("saved", len(df), "rows")