import os

import pytest
import subprocess

@pytest.fixture
def sensor_env():
   #Install sensor before test, remove after.
    subprocess.run(["sudo", "dpkg", "-i", "/opt/falcon.pkg"], capture_output=True, timeout=120)
    yield
    subprocess.run(["sudo", "apt-get", "remove", "-y", "falcon-sensor"], capture_output=True)

@pytest.mark.smoke
def test_service_is_active(sensor_env):
    result = subprocess.run(["systemctl", "is-active", "falcon-sensor"], capture_output=True, text=True)
    assert result.stdout.strip() == "active", "Sensor service not active"

def test_process_is_running(sensor_env):
    result = subprocess.run(["pgrep", "-x", "falcond"], capture_output=True, text=True)
    assert result.returncode == 0, "falcond process not found"

def test_version_matches(sensor_env):
    result = subprocess.run(["/opt/CrowdStrike/falconctl", "-g", "--version"], capture_output=True, text=True)
    assert result.returncode == 0
    parts = result.stdout.strip().split(".")
    assert len(parts) >= 2, f"Unexpected version format: {result.stdout.strip()}"

