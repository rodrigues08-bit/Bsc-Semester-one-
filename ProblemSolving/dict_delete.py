pairs = []

n = int(input("How many key-value pairs? "))

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    pairs.append((key, value))

d = dict(pairs)

print("Dictionary:", d)

delete_key = input("Enter the key you want to delete: ")

del d[delete_key]

print("Dictionary after deletion:", d)

#for syntax
# Dictionary
student = {
    "name": "John",
    "age": 20,
    "course": "Python",
    "marks": 85,
    "city": "Goa"
}

print("Original dictionary:")
print(student)


# --------------------------------
# 1. del
# --------------------------------
# Deletes a specific key-value pair

del student["city"]

print("\nAfter del:")
print(student)


# --------------------------------
# 2. pop()
# --------------------------------
# Deletes a specific key-value pair
# and returns the value that was deleted

removed = student.pop("age")

print("\nDeleted value:", removed)
print("After pop():")
print(student)


# --------------------------------
# 3. popitem()
# --------------------------------
# Deletes the LAST key-value pair

removed_item = student.popitem()

print("\nDeleted item:", removed_item)
print("After popitem():")
print(student)


# --------------------------------
# 4. clear()
# --------------------------------
# Deletes ALL key-value pairs

student.clear()

print("\nAfter clear():")
print(student)