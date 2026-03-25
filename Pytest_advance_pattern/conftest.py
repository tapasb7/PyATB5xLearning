import pytest
import subprocess

@pytest.fixture(scope='session')
def sensor_fleet():
    #Available to ALL tests. Set up once per test run
    fleet = {
        "linux-01": {"ip": "192.168.1.10", "os": "ubuntu", "port": 22},
        "linux-02": {"ip": "192.168.1.11", "os": "centos", "port": 22},
        "win-01": {"ip": "192.168.1.20", "os": "windows", "port": 5985},
    }
    yield fleet
    # Session teardown: verify all sensors uninstalled after all tests
    print('\nSession Complete - all tests done')

@pytest.fixture(scope='function')
def install_sensor(sensor_fleet):
    target = sensor_fleet['linux-01']
    subprocess.run(['sudo','dpkg -i','/opt/sensor.pkg'],
                   capture_output=True,
                   timeout=10
                   )
    yield target
    subprocess.run(['sudo','apt-get','remove','falcon-sensor'],
                   capture_output=True,)

