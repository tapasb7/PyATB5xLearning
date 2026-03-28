# Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21...
# Each number = sum of the previous two.
# Like a staircase where each step height = sum of previous two.

n = int(input('Input the range : '))
a = 0
b = 1
c = 0
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    for i in range(n):
        print(c,end=' ')
        a = b
        b = c
        c = a + b