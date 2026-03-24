n = int(input('enter number: '))

def all_square_pattern(n):
    for i in range(n):
        for j in range(n):
            print('*',end="  ")
        print()

def decrease_pattern(n):
    for i in range(n):
        for j in range(i,n):
            print('*',end=" ")
        print()

def increase_pattern(n):
    for i in range(n):
        for j in range(i+1):
            print('*',end=" ")
        print()

def combine_pattern(n): #decreasing space + increasing '*'
    for i in range(n):
        for j in range(i,n):
            print(' ',end=" ")
        for j in range(i+1):
            print('*',end=" ")
        print()


def hill_pattern(n): #decreasing space + increasing '*' + increasing *
     for i in range(n):
         for j in range(i, n):
             print(' ', end=" ")
         for j in range(i):
             print('*', end=" ")
         for j in range(i + 1):
             print('*', end=" ")
         print()


def reverse_hill_pattern(n):
    for i in range(n):
        for j in range(i + 1):
            print(' ', end=" ")
        for j in range(i, n-1):
            print('*', end=" ")
        for j in range(i, n):
            print('*', end=" ")

        print()

def diamond_pattern(n):
    for i in range(n-1):
        for j in range(i, n):
            print(' ', end=" ")
        for j in range(i):
            print('*', end=" ")
        for j in range(i + 1):
            print('*', end=" ")
        print()
    for i in range(n):
        for j in range(i + 1):
            print(' ', end=" ")
        for j in range(i, n-1):
            print('*', end=" ")
        for j in range(i, n):
            print('*', end=" ")
        print()





# print('Now Select pattern...')
# print('1. hill')
# print('2. decrease')
# print('3. increase')
# print('4. combine')
# print('5. reverse_hill')
# print('6. diamond')


#all_square_pattern(n)
#increase_pattern(n)
#combine_pattern(n)
#hill_pattern(n)
#reverse_hill_pattern(n)
diamond_pattern(n)

