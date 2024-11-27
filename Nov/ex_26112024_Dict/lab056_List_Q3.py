# Write a Python program that takes two lists and
# returns True if they have at least one common member.
#commit & push


list_1 = ["Avinash", "Vivian", "Isha", "Bagga", "Sindey"]
list_2 = ["Karan", "Chum", "Shilpa", "Shruthika", "Digvijay"]

if ((set(list_1).intersection(set(list_2)))) != set():
    print(True)
else:
    print(False)

