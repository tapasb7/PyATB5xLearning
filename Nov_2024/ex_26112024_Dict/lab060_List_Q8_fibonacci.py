# Write a Python program to get the Fibonacci series between 0 to 50.


def _fib_series(n):
    result_list = []
    num_1 = 0
    num_2 = 1
    for i in range(n):
        result_list.append(num_1)
        num_1 , num_2 = num_2 , num_1 + num_2 # this line can be also assigned as below
        # num_3 = num_1 + num_2
        # num_1 = num_2
        # num_2 = num_3

    return result_list

num_range = 50
print(_fib_series(num_range))
