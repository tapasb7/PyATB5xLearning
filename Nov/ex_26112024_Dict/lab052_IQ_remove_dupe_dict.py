# remove duplicate values from dictionary

my_dict = {"a":1, "b":2, "c":1, "d":4, "e":1}

result = {}
unique_value = set()
for key, value in my_dict.items():
    if value not in unique_value:
        result[key] = value
        unique_value.add(value)
print(result)