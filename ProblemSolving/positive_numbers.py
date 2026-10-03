numbers = []

n = int(input("How many numbers? "))

for i in range(n):
    x = int(input("Enter number: "))
    numbers.append(x)

positive = []

for x in numbers:
    if x > 0:
        positive.append(x)

print("Positive numbers:", positive)