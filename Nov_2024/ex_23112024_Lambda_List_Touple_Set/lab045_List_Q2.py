# Write a Python program to count the number of strings
# in a list where the string length is 2 or more
# and the first and last characters are the same.

my_list = ["swiss", "avacado", "madam", "rr", "pepper"]
# print(my_list[-1])



def _verify_string_(my_list):
    ctr = 0
    for i in my_list:
        if len(i) >= 2 and i[0] == i[-1]:
            ctr += 1
    return ctr


print("Ans is : ", _verify_string_(my_list))


