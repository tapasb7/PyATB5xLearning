# Write a Python program to find the factorial of a number
# i/o

num = int(input("Enter the number : "))
_fact_list = []

def find_fact_list(num):


    for i in range(num, 0, -1):
        _fact_list.append(i)
    return _fact_list


find_fact_list(num)


def multi(_fact_list):
    res = 1
    for i in _fact_list:
        res = res * i
    return res


print("The factorial of ", num, "is : ", multi(_fact_list))
