import random
import numpy as np
import pandas as pd
import math

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

students = []

for i in range(5):
    marks = random.randint(30, 100)
    students.append(Student("Student"+str(i), marks))

data = []

for s in students:
    if s.marks >= 75:
        grade = "A"
    elif s.marks >= 50:
        grade = "B"
    else:
        grade = "C"

    data.append([s.name, s.marks, grade])

df = pd.DataFrame(data, columns=["Name", "Marks", "Grade"])

print(df)

print("Mean:", np.mean([s.marks for s in students]))

file = open("report.txt", "w")
file.write(str(df))
file.close()
