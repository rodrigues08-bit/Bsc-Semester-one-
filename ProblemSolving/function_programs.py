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