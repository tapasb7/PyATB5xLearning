fleet = {
    "linux-01": {"ip": "192.168.1.10", "os": "ubuntu", "sensor": False},
    "linux-02": {"ip": "192.168.1.11", "os": "centos", "sensor": True},
    "win-01":   {"ip": "192.168.1.20", "os": "windows","sensor": False},
}

# Find servers without sensor

for key, value in fleet.items():
    if value["sensor"] == False:
        print(key)
    else:
        pass