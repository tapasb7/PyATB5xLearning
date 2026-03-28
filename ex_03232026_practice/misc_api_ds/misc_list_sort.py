# Sort by custom key — sort list of dicts by a field

fleet = [
    {"hostname": "win-01",   "cpu": 87},
    {"hostname": "linux-01", "cpu": 23},
    {"hostname": "win-02",   "cpu": 65},
    {"hostname": "win-05",   "cpu": 53}
]

print(sorted(fleet, key=lambda x: x["cpu"], reverse=True), end=' ')
print('\n\n')

# Sort list of tuples by second element
results = [("linux-01", 0, 501), ("win-01", 2, 201), ("linux-02", 1, 130)]
print(sorted(results, key=lambda x: x[1]))

