n = int(input("Enter the number of terms (n): "))
S = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        S -= i
    else:
        S += i
print(f"Sum of the series up to {n} terms is: {S}")