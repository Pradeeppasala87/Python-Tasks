
subjects = ("Math", "Science", "English")

student_names = set()

student_marks = {}


def calculate_total(marks_list):
    if len(marks_list) == 0:
        return 0
    return marks_list[0] + calculate_total(marks_list[1:])


def add_student():
    name = input("Enter student name: ")

    marks = []
    try:
        for subject in subjects:
            mark = input(f"Enter marks for {subject}: ")
            if not mark.isdigit():
                raise ValueError
            marks.append(int(mark))

        student_names.add(name)
        student_marks[name] = marks
        print("Student added successfully!")

    except ValueError:
        print("Invalid input! Please enter numeric marks.")


def display_students():
    if not student_marks:
        print("No records found.")
    else:
        for name, marks in student_marks.items():
            print(f"{name} : {marks}")



def calculate_average():
    try:
        name = input("Enter student name to calculate average: ")

        if name not in student_marks:
            raise NameError

        marks = student_marks[name]

        total = calculate_total(marks)

        average = total / len(marks)  

        print("Total Marks:", total)
        print("Average Marks:", average)

    except NameError:
        print("Student name not found.")

    except ZeroDivisionError:
        print("Cannot divide by zero.")

    except TypeError:
        print("Marks data type error.")



def main():
    while True:
        print("\n1. Add Student")
        print("2. Display Students")
        print("3. Calculate Average")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            calculate_average()
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")


# Run the program
main()
