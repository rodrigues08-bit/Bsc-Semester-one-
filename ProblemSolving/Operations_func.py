def operations(x, y):
    print("Sum:", x + y)
    print("Difference:", x - y)
    print("Product:",x *y)
    
    # Check if the second number is zero to avoid a division error
    if y != 0:
        print("Division:",x / y)
    else:
        print("Division: Cannot divide by zero!")

# Get input from the user and convert it to floating-point numbers
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

print() # Adds a blank line for readability

# Call the function with the user's numbers
operations(x,y)