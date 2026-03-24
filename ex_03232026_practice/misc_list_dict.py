# Q: "Given a list of server results,
# build a dict showing pass/fail per server"

results = [
    {"server": "linux-01", "exit_code": 0, "os": "ubuntu"},
    {"server": "linux-02", "exit_code": 1, "os": "ubuntu"},
    {"server": "win-01",   "exit_code": 0, "os": "windows"},
    {"server": "win-02",   "exit_code": 2, "os": "windows"},
]

summary = dict()

for i in results:
    if i['exit_code'] != 0:
        summary[i['server']] = 'Pass'
    else:
        summary[i['server']] = 'Fail'
print(summary)
