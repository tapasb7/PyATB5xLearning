#Python program to create a generation calculator.
#input is birth year, output is which generation it belongs to.
# There are several generations of humans, including:
# The Greatest Generation: Born between 1901 and 1927,
# The Silent Generation: Born between 1928 and 1945.
# Baby Boom Generation: Born between 1946 and 1964.
# Generation X: Born between 1965 and 1980,
# Millennial Generation or Generation Y: 1981 and 1996
# Generation Z or iGen: Born between 1997 and 2010,
# Generation Alpha: Born between 2010 and 2024.
from idlelib.pyparse import trans
from pickle import PROTO

# match parameter:
#     case pattern1:
#         # code for pattern 1
#     case pattern2:
#         # code for pattern 2
#     .
#     .
#     case patterN:
#         # code for pattern N
#     case _:
#         # default code block

yob = int(input("Enter your YOB :\t"))
age = int(2024 - yob)

print("Your age is :", age)
if yob in range(1901,1928):
    print("You are The Greatest Gen")
elif yob in range(1928,1945):
    print("The are The Silent Gen")
elif yob in range(1946,1965):
    print("The are a Baby-boom")
elif yob in range(1965,1981):
    print("The are the Gen-X")
elif yob in range(1981,1997):
    print("The are a 90s Kid, Like me :)")
elif yob in range(1997,2011):
    print("The are a Gen-Z")
elif yob in range(2010,2025):
    print("The are a Gen-Alpha")
else:
    print("Calculator is not for you")
