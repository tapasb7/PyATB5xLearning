# Print the bellow pattern using Loop
# *
#
# **
#
# ***
#
# ****
#
# *****

n = 5

def right_triangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("* ", end="")
        print("")

right_triangle(n)


print("===============================")

# Function to print inverted half pyramid pattern
def inverted_half_pyramid(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print("* ", end="")
        print("\r")

# Example: Inverted Half Pyramid with n = 5

inverted_half_pyramid(n)