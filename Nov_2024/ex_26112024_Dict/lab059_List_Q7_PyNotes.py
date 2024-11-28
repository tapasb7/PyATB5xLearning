# Write a Python program that
# prints all the numbers from 0 to 6 except 3 and 6.

result = []

for i in range(0, 7):
    if i == 3 or i == 6:
        pass
    else:
        result.append(i)
print(result)
