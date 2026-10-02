"""
Name: Robert Galletta
File: classify_triangle.py
Date: 10-2-2026
Description: This program classifies triangles based on the lengths of their sides. 
It checks for invalid input, determines if the sides can form a triangle, 
and classifies the triangle as Equilateral, Isosceles, or Scalene. 
Additionally, it checks if the triangle is a right triangle.
"""
def classify_triangle(a, b, c):
    """
    Input: a, b, c are the lengths of the three sides of a triangle.
    Output: A list containing two strings
    """
    properties = ['','']
    if a <= 0 or b <= 0 or c <= 0:
        properties[0] = 'InvalidInput'
    elif a + b <= c or a + c <= b or b + c <= a:
        properties[0] = 'NotATriangle'
    elif a == b == c:
        properties[0] = 'Equilateral'
    elif a == b or b == c or a == c:
        properties[0] = 'Isosceles'
    else:
        properties[0] = 'Scalene'

    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        properties[1] = 'Right'
    else:
        properties[1] = 'NotRight'

    return properties

def main():
    """
    This function prompts the user to input the lengths of the three sides of a triangle,
    calls the classify_triangle function, and prints the classification of the triangle.
    """
    a = int(input("Enter the length of side a: "))
    b = int(input("Enter the length of side b: "))
    c = int(input("Enter the length of side c: "))
    result = classify_triangle(a, b, c)
    print(f"The triangle is classified as: {result[0]} and {result[1]}.")

main()
