# Without Temporary Variable
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
print("The original values are: ",a, b)
a,b=b,a
print("The swapped values are: ",a, b)
