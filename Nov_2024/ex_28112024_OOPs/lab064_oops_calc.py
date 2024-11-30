class cal:
    # attributes
    a = None
    b = None

    # init func
    def __init__(self):
        print("DC")

    # behaviour
    def sum(self, a, b):
        return (a + b)

    def sub(self, a, b):
        return (a - b)

    def div(self, a, b):
        return (a / b)

    def mul(self, a, b):
        return (a * b)


# obj_reference
obj_ref = cal()

a = float(input("Enter value of a :"))
b = float(input("Enter value of b :"))

sum_result = obj_ref.sum(a, b)
sub_result = obj_ref.sub(a,b)
div_result = obj_ref.div(a,b)
mul_result = obj_ref.mul(a,b)

print(sum_result, sub_result, div_result, mul_result)
