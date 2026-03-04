
students = []
for i in range(3):
    print(f"Enter name {i + 1}")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    grade = input("Enter Grade: ")
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
