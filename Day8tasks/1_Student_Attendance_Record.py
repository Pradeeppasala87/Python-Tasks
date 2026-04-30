name = input("Enter student name: ")


with open("attendance.txt", "a") as file:
    file.write(name + "\n")


print("\nAttendance List:")
with open("attendance.txt", "r") as file:
    print(file.read())
