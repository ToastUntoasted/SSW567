def classify_triangle(a, b, c):
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
    a = int(input("Enter the length of side a: "))
    b = int(input("Enter the length of side b: "))
    c = int(input("Enter the length of side c: "))
    result = classify_triangle(a, b, c)
    print(f"The triangle is classified as: {result[0]} and {result[1]}.")

main()