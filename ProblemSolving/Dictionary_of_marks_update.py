students = {
    "Rahul": 85,
    "Priya": 90,
    "Amit": 78
}

print("Original dictionary:")
print(students)

name = input("Enter student name to update: ")
marks = int(input("Enter new marks: "))

if name in students:
    students[name] = marks
    print("Value updated successfully.")
else:
    print("Student not found.")

print("Updated dictionary:")
print(students)