my_dict = {
    "Name": "Tapas",
    "Age": 34,
    "Address": "Bangalore",
    "SSN_Num": "03456785423",
    "Experience" : 10,
    "Role" : "SDET",
}

print(my_dict)

del my_dict["Age"]
my_dict["Education"] = "Post Graduate"
print(my_dict)
print(my_dict["Role"])

print("Age" in my_dict)

print(my_dict.values())
print(my_dict.keys())
print(my_dict.items())

