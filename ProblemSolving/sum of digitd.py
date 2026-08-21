n=int(input("Enter a number: "))
print ("The initial given number is:",n)
t=0
while n > 0:
    r = n % 10
    t = t + r
    n = n // 10
print("Sum of digits:", t)
    
