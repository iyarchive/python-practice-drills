import pandas as pd

df = pd.DataFrame({
    "name": ["Alex", "Axel", "Amy", "Andrea", "Alexis"],
    "grade": [2.25, 3.00, 3.25, 1.00, 1.50],
    "units": [25, 27, 19, 20, 23]
})

df["status"] = ["Passing" if g < 3.00 else "Failing" for g in df["grade"]]

print(df)
