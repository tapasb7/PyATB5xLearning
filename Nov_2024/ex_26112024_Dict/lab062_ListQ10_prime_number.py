# Write a Python program to check if a number is a prime number


num = int(input("Enter number : "))


def check_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print("Not prime")
                break
        else:
            print("Yes it is prime")
    else:
        print("Invalid number")

check_prime(num)



