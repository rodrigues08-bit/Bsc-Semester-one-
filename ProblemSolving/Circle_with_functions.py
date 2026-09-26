import math

def compute_circle(r):
    area = math.pi * r ** 2
    circumference = 2 * math.pi * r
    print(f"Area of the circle: {area:.2f}")
    print(f"Circumference of the circle: {circumference:.2f}")

radius = float(input("Enter the radius of the circle: "))
compute_circle(radius)