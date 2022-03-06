import numpy as np
import pandas as pd

nam = ["Sam", "Shila", "Jiten", "Raj"]
no_ = [91, 89, 76, 55]
names = pd.Series(nam)
marks = pd.Series(no_)
stud = {"Names": names, "Marks": marks}
df = pd.DataFrame(stud, columns=["Names", "Marks"])
df["Grade"] = np.NaN
print("Initial values in dataframe")
print(df)
for (col, colseries) in df.iteritems():
    length = len(colseries)
    if col == "Marks":
        lstMarks = []
        for row in range(length):
            mrks = colseries[row]
            if mrks >= 90:
                lstMarks.append("A+")
            elif mrks >= 70:
                lstMarks.append("A")
            elif mrks >= 60:
                lstMarks.append("B")
            elif mrks >= 50:
                lstMarks.append("C")
            elif mrks >= 40:
                lstMarks.append("D")
            else:
                lstMarks.append("F")

df["Grade"] = lstMarks
print("\n\nDataFrame after calcution of Grades")
print(df)
