import pandas as pd

df = pd.DataFrame({
    "name": ["Aya", "Linda", "Vivi", "Zack", "Elena"],
    "age": [20, 20, 21, 25, 23],
    "course": ["BSAM", "BSCS", "BSIT", "BSAM", "BSIT"],
    "grade": [1.50, 2.00, 1.75, 2.50, 1.00]
})

print(df[df["grade"] < 2.00])

print(df[df["course"] == "BSAM"])

print(df[(df["age"] == 20) & (df["course"] == "BSIT")])
