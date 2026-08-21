x=int(input("Enter a number to print Fibonacci Series: "))
p=0
c=1
for i in range(x):
    print(p,",",end="")
    n=p+c
    p=c
    c=n
   
