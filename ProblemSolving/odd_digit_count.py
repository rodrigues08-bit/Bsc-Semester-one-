number = input("Enter a number: ")

count = 0
print("Odd digits:")
for digit in number:
    if int(digit) % 2 != 0:
        print(digit)
        count = count + 1

print("Odd digits count:", count)
