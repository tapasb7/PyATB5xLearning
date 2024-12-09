#To handle an exception use try-except

print("------------Start of Program---------------")
try:
    a = int(input("Enter number A : "))
    b = int(input("Enter number B : "))
    c = a / b

except Exception as e:
    print(e)

else:
    print("result is : ", c)

finally:
    print("--------End of Program-----------")
