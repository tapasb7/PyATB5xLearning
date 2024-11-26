dict_1 = {"a": 1, "b": 2, "c" : 5}
dict_2 = {"a": 1, "b": 2}

missing_keys = set(dict_1.keys()) - set(dict_2.keys())
print(missing_keys)


