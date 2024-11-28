d_mart = ["Biscuits", "Rice", "Shampoo", "Conditioner", "Mixture"]
mk_ahmed = ["Moong", "Mususr", "Tur", "Navaratna"]
num_list = [1 , 2, 55, 67, 23, 56, 7, 54, 35, 8, 36]
print(d_mart)
print(mk_ahmed)
# length
print(len(d_mart))

# append, length increased after append a value
d_mart.append("Oil")
print(len(d_mart))

# extend
d_mart.extend(["Rice", "Atta", "Banana"])
print(d_mart)
print(d_mart.count("Rice"))

# insert
d_mart.insert(1, "Cake")
print(d_mart)

# #remove Rice
d_mart.remove("Rice")
print(d_mart.count("Rice"))
print(d_mart)

print(d_mart[3])
d_mart[3] = "Dove-Conditioner"
print(d_mart[0])

for i in d_mart:
    print(i)



print(num_list, end =  "\n")
num_list.sort()
print(num_list)