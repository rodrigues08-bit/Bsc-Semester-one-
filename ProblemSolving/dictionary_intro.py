n = int(input("Enter number of key-value pairs: "))

d = {}

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value

print(d)

#using dict()
d = dict()
n = int(input("How many key-value pairs? "))

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value

print(d)

pairs = []

n = int(input("How many key-value pairs? "))

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    pairs.append((key, value))

d = dict(pairs)

print(d)