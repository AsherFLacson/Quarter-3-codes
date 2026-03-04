
students = []
for i in range(3):
    print(f"Enter information for Student {i + 1}")
    name = input("Name: ")
    age = input("Age: ")
    grade = input("Grade: ")
    student = {
        "Name": name,
        "Age": age,
        "Grade": grade
    }
    students.append(student)
for student in students:
    print("Name:", student["Name"])
    print("Age:", student["Age"])
    print("Grade:", student["Grade"])
