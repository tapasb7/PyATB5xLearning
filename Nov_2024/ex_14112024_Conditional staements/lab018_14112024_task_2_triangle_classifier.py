# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal),
# or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.

# determine Input section

a = int(input("enter length of side-A\n"))
b = int(input("enter length of side-B\n"))
c = int(input("enter length of side-C\n"))

# rough logic
if a > b and b > 0 and c > 0:
    if a + b > c and b + c > a and a + c > b:

        if a == b and b == c:
            print("equilateral.. all sides are equal")
        elif a == b or a == c or b == c:
            print("isosceles.. exactly two sides are equal")
        else:
            print("scalene.. no sides are equal")
    else:
        print("Not forming Triangle")
else:
    print("Not valid Length")
