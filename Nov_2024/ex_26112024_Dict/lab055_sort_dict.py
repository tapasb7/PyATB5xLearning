# Sort a dictionary by its values in ascending order
# output --> {b: 1 , c: 2 , a :3}


my_dict = {"a": 3, "b": 1, "c": 2}

print(sorted(my_dict.items()))

print(dict(sorted(my_dict.items(), key = lambda my_dict : my_dict[1] )))


print(dict(sorted(my_dict.items(), key = lambda my_dict : my_dict[1], reverse= True )))
#
# for key, value in my_dict.items():
#     if value is max(my_dict.values()):
#         print(key)
#         my_dict.pop(key)
#         result[key] = value





