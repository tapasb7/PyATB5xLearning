# Write a program that calculates and displays the letter grade
# for a given numerical score (e.g., A, B, C, D, or F)
# based on the following grading scale:
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59


mark = int(input("Enter your marks received\n"))

if mark >= 90 and mark <=100:
    print("Your Grade is A")
elif mark >= 80 and mark <=89:
    print("Your grade is B")
elif mark >= 70 and mark <=79:
    print("Your grade is C")
elif mark >= 60 and mark <= 69:
    print("Your grade is D")
elif mark > 100:
    print("Come on! Don't lie ")
else:
    print("Grade is F")