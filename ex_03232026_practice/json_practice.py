import json

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

with open('student_info.json', 'w') as fp:
    json.dump(student_info, fp)

print(student_info)