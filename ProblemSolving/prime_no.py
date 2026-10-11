#  Check if a given number is prime ---
num = int(input("Enter a number to check if it is prime: "))

if num > 1:
    # Check for factors from 2 up to the number itself
    for i in range(2,num):
        if num % i == 0:
            print(num, "is not a prime number.")
            break
    else:
        # The 'else' block runs if the loop finishes without breaking
        print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")

print("\n------------------------------------------------")
print("Prime numbers less than 100:\n")

#  Generate prime numbers less than 100 ---
for n in range(2, 100):
    # Same logic as above
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        # If the loop didn't break, 'n' is prime. 
        # end=" " prints them on the same line with a space instead of a new line
        print(n, end=" ")

print() # Adds a final blank line