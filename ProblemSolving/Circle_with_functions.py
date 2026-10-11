import math

def circle(radius):
    # Calculate area (pi * r^2)
    area = math.pi * (radius ** 2)
    
    # Calculate circumference (2 * pi * r)
    circum = 2 * math.pi * radius
    
    # Display the results
    print("Area of the circle:", area)
    print("Circumference of the circle:", circum)

# Get the radius from the user
r = float(input("Enter the radius of the circle: "))

print() # Adds a blank line for readability

# Pass the input to the function
circle(r)