text = "Bamboozled"

print(text[0:2])
print(text[-2::])
print(text[8::])
print(text[2::])
print(text[-8::])

for i in range(2, 10):
    print(text[i], end="")
print()

print(text[::-3])
print(text[0:6])

for i in range(0, 6):
    print(text[i], end="")
print()

print(text[0::])
print(text[::-1])
print(text[0:10:2])
print(text[0:10:2])
print(text[0:10:2])
print(text[0:10:3])
print(text[0:10:4])

x = "Hype!"
print(text + x)

y = "Monger"
print(text + x)