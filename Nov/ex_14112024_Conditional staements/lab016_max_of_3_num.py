# Find the maximum of three numbers
# take float inputs from user

# take input section
num1 = float(input("Enter first number\n"))
num2 = float(input("Enter second number\n"))
num3 = float(input("Enter third number\n"))

# logic section include if,elif statement

if num1 >= num2 and num1 >= num3:
    print(num1, " is maximum of three")
elif num2 >= num3 and num2 >= num1:
    print(num2, " is maximum of three")
else:
    print(num3, " is the max of all three numbers")
#commit this code to github