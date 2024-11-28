# check if age above 21 then only eligible for club

age = int(input("How old are you??\n"))

if age >= 21 and age <= 110:
    print("Welcome to the club.")
elif age >= 110 or age < 0:
    print("You're not Human.. Not allowed!!")
else:
    print("Sorry!! minors are not allowed.")
