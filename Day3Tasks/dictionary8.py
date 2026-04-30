students = {
    "pradeep": 78,
    "Bobby": 72,
    "francis": 78,
    "praveen": 98
}

highest_marks = 0
top_student = ""

for name, marks in students.items():
    if marks > highest_marks:
        highest_marks = marks
        top_student = name

print("Top student:", top_student)
print("Highest marks:", highest_marks)
