#
my_list = [88, 5, 8, 9, 11, 2, 19, 58]
n = len(my_list)

for i in range(n):
    for j in range(n - i - 1):
        if my_list[j] > my_list[j + 1]:
            temp = my_list[j]
            my_list[j] = my_list[j + 1]
            my_list[j + 1] = temp


print(my_list)