for i in range(1,5):
    for j in range(1,5):
        print(j,end="")
    print() 
print()
print()
for i in range(1,5):
    for j in range(1,i):
         print(j,end="")
    print()  
print()
print()
for i in range(1,7):
    for j in range(1,i):
         print("*",end="")
    print() 
print()
print()
for i in range(1,9):
    for j in range(1,i):
        if j%2==0:
            print("+",end="")
        else:
            print("*",end="")
    print() 
print()
print()
for i in range(1, 8):
    if i % 2 == 1:
        print("*" * i)
    else:
        print("+" * i)

print()
print()
for i in range(1, 8):
    if i % 2 == 1:
        print(""*(7-i)+"*" * i)
    else:
        print(""*(7-i)+"+" * i)
    print()
print()
print()
for i in range(1, 7):
    print("  " * (6 - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")

    print()  
print()
print()
for i in range(1, 6):
    print(" " * (9 - (2 * i - 1)), end="")
    for j in range(1, 2 * i):
        print(j, end=" ")

    print()  
 