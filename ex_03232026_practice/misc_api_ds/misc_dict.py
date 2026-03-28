server = {
    "hostname": "linux-01",
    "ip": "192.168.1.10",
    "os": "Ubuntu 22.04",
    "sensor_installed": False,
    "port": 22,
    'identification': {
        'serial_number': 'DL360PNB12345AT0087646',
        'model': 'HPE DL360'
    },
    'storage' : {
        'disk_usage_tb': 1024,
        'disk_usage_fs': 300,
        'form_factor': 'SSD'
    }
}

print(server['identification']['serial_number'])
server["sensor_installed"] = True
server["firmware_version"] = '3.14.3'
# print(server, end='')

for key, value in server.items():
    print(f"{key}: {value}")