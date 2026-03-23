fruits = ["Apple", "Banana", "Cherry", "Dragonfruit", 'Apple_galaxy', 'Apple_wood', 'Apple_shimla']
scores = [85, 92, 78, 100, 64]
user_profile = ["Alex", 28, 5.11, True]
servers = ["linux-01", "linux-02", "win-01", "win-02"]

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

student_records = [
    ["Alex", 28, 5.11, True, 'UK'],
    ["Sam", 22, 5.8, False, 'USA'],
    ["Casey", 31, 6.0, True, 'Canada'],
    ["Rajesh", 29, 5.10, True, 'India']
]

for i, fruit in enumerate(fruits):
    print(i, fruit)

fruits_result = [i for i in fruits if "Apple" in i]
print(fruits_result)

servers.append('linux-03')
servers.insert(0, 'gateway')
print(len(servers))
print(servers)

print('gateway' in servers)
print(servers.index('gateway'))

# print(numbers[4:9])
# print(student_records[3])
# print(fruits[0:3])
# #print(fruits[0])
# # print(servers[-1])
# print(servers[1:3])