import math


students = [("Arjun", 65), ("Bala", 45), ("Charan", 78)]


data = dict(students)


print("Above 50:")
for name, marks in data.items():
    if marks > 50:
        print(name, marks)


total = sum(data.values())
avg = math.floor(total / len(data))

print("Average:", avg)


file = open("result.txt", "w")

file.write("Students Data\n")
for name, marks in data.items():
    file.write(name + " " + str(marks) + "\n")

file.write("Average: " + str(avg))

file.close()

print("Saved to file")

