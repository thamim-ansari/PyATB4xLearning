# Task 8

# Write a program that classifies a triangle based on its side lengths.

# Given three input values representing the lengths of the sides,

# determine if the triangle is equilateral (all sides are equal),

# isosceles (exactly two sides are equal), or scalene (no sides are equal).

# Use an if-else statement to classify the triangle.

side1 = int(input("Enter side1: "))
side2 = int(input("Enter side2: "))
side3 = int(input("Enter side3: "))

if side1 == side2 and side2 == side3:
    print("Equilateral")
elif side1 == side2 or side2 == side3 or side3 == side1:
    print("Isosceles")
else:
    print("Scalene")
