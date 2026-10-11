#for factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

num = int(input("Enter a number: "))
print("Factorial =", factorial(num))

#for Fibonacci series
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

num = int(input("Enter the number of terms: "))
fibonacci(num)  

#to Get factors
def factors(number):
    factors = []
    # Loop from 1 up to the number itself
    for i in range(1, number + 1):
        # If the remainder is 0, 'i' is a factor
        if number % i == 0:
            factors.append(i)
    return factors

# Get input from the user and convert it to an integer
u = int(input("Enter a number to find its factors: "))

# Call the function and store the result
result =factors(u)

print("Factors of", u, "are:", result)

#to check even or odd
def check(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Get input from the user and convert it to an integer
x = int(input("Enter a number: "))

# Call the function
result = check(x)

# Print the result
print(x, "is an", result, "number.")