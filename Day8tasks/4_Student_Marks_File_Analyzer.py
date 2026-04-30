

total = 0
count = 0

with open("marks.txt", "r") as file:
    print("Student Records:\n")
    
    for line in file:
        name, marks = line.split()
        marks = int(marks)
        
        print(f"Name: {name}, Marks: {marks}")
        
        total += marks
        count += 1

if count > 0:
    average = total / count
    print("\nAverage Marks:", average)
else:
    print("No records found.")
