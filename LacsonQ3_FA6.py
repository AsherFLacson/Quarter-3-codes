

name = (input("Enter your name: "))
age = int(input("Enter your age: "))
FS = (input("Enter your favourite subject: "))

student = { "Name": name,
    "Age": age,
    "Favorite Subject": FS
    }
print(student)

#or 

print("Student Record")
print("Name:", student["Name"])
print("Age: ", student["Age"])
print("Favourite Subject: ", student["Favorite Subject"])