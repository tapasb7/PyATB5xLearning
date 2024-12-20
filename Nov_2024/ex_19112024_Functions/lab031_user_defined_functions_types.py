# User Defined
# 1. They can't return anything, non-return
# 2.They can return something
# 3.They have parameters
# 4. They don't parameters / arguments


# type-1 : No parameter/arguments & no return type
def type_1():
    print("This is function type-1 one call")


type_1()


# type-2 : With parameter/arguments & no return type
def type_2(name):
    print("hello ", name, " You are in function type-2")


type_2("Tapas")


# type-3 : With default parameter/arguments & no return type (aka positional parameter)
def type_3(name1="Tapas", name2="Ronaldo", name3="Jayden"):
    print("function type-3 call --> The names are \t", name1, name2, name3)


type_3()
type_3(name1="Rakesh")
type_3(name1="Amar", name2="Akbar", name3="Anthony")


# type-4 : With parameter/arguments & with return type
def type_4_sum(a, b):
    return a + b


result = type_4_sum(10, 20)  # type_4_sum function called here and output are stored in "result" variable
print("function type-4 call --> sum is", result)
# type_4_sum() #not required, function is already called
