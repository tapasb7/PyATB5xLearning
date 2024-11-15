# Find the LeapYear
# Leap day occurs in each year that is a multiple of 4,
# except for years evenly divisible by 100 but not by 400. This is from wikepedia


# but A year is a leap year if “any one of ” the following conditions are satisfied:
#
# The year is multiple of 400.
# The year is a multiple of 4 and not a multiple of 100.


# # take input section
year = int(input("Enter the Year :\n"))

# # logic section include if,elif statement

if (year % 400) == 0 and (year % 4) == 0 or (year % 100) != 0:
    print(year, " is a Leap Year")
else:
    print(year, " is not a Leap Year")

