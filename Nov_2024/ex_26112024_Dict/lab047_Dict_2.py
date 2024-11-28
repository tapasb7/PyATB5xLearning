
student_info = {
    "name" : "Sujan",
    "branch" : "IT",
    "year" : 2,
    "age" : 21,
    "address" : {
        "local_address" : "MG Road",
        "permenant_address" : "Katihar"
    }
 }

print(student_info["name"])
print(student_info)

student_info_2 = dict(name = "Nazim", branch = "Mechanical", year = 3, age = 23, address = "MH")

print(student_info_2)

student_list = [student_info, student_info_2]
print(student_list)

print(student_list[0]["name"])
print(student_list[0]["address"]["local_address"])
print(student_list[1]["name"])