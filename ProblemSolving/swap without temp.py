# Without Temporary Variable
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
print("The original values are: ",a, b)
a=a+b
b=a-b
a=a-b
print("The swapped values are: ",a, b)
