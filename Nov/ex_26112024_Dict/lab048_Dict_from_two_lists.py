# Dict from two lists


keys = ["name", "role", "exp"]
value = ["Karan", "Actor", 20]

my_dict = dict(zip(keys, value))
print(my_dict)

# Merge two dict
dict_1 = {"a": 1, "b": 2}
dict_2 = {"c": 3, "d": 4}

merged_dict = dict_1 | dict_2
print(merged_dict)
print(merged_dict["c"])
print(merged_dict.get("b"))