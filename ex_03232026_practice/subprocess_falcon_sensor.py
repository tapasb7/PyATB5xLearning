#Practical EDR examples

import subprocess

#check if sensor running
def is_sensor_running():
    result = subprocess.run(
        ['systemctl', 'is-active', 'falcon-sensor.service'],
        capture_output=True,
        text=True
    )
    return result.stdout.strip() == 'active'

#install sensor using package
def install_sensor(package_path):
    result = subprocess.run(
        ['sudo', 'dpkg', '-i', package_path],
        capture_output=True,
        text=True,
        timeout=120
    )
    return result.returncode == 0, result.stdout, result.stderr

#uninstall sensor
def uninstall_sensor(package_path):
    result = subprocess.run(
        ['sudo', 'apt-get', 'remove', '-y', 'falcon-sensor'],
        capture_output=True,
        text=True,
        timeout=120
    )
    return result.returncode == 0



