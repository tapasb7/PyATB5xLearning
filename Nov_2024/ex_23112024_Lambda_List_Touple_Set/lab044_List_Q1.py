# Write a Python program to
# find the largest number in a list.


list_1 = [5, 1, 34, 23, 56, 23, 78, 15, 9, 67, 3]
print(list_1)

# list_1 = list_1.sort()
list_1.sort()
print(list_1)

print("Largest number in the list is : ", list_1[-1])

# find the largest number in a list
print("Smallest number in the list is : ", list_1[0])

# sum of all numbers

print("Sum of numbers : ", sum(list_1))


# multiply all numbers

def multi(list_1):
    res = 1
    for i in list_1:
        res = res * i
    return res


print("Multiplication of numbers : ", multi(list_1))
