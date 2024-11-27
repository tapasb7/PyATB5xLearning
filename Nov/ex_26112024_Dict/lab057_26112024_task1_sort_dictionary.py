# Sort a dictionary by its values in descending order
# output --> {b: 1 , c: 2 , a :3}
#commit & push

my_dict = {"a": 3, "b": 1, "c": 2}

my_list = list(my_dict.values())
# print(my_list)
my_list.sort(reverse=True)
# print(my_list)

result = {}

for item in my_list:
    for key, value in my_dict.items():
        if  item == value:
            result[key] = value
print(result)
