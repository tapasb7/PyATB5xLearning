# Q: "Write Python to check if a service is running
# and return its PID"


import subprocess
import re


# Returns dict with status and PID, or None if not running
def get_service_info(service_name):
    try:
        result = subprocess.run(
            ['systemctl', 'status', service_name],
            capture_output=True,
            text=True,
            timeout=10
        )

        info = {
            'service_name': service_name,
            'active': False,
            'pid' : None
        }

        for line in result.stdout.splitlines():
            line = line.strip()
            if "Active:" in line:
                info['active'] = True
            if 'Main PID:' in line:
                pid_match = re.search('Main PID:\s*(\d+)', line)
                if pid_match:
                    info['pid'] = int(pid_match.group(1))

        return info
    except subprocess.TimeoutExpired:
        return {'service_name': service_name, 'error': 'Timed out'}
    except Exception as e:
        return {'service_name': service_name, 'error': str(e)}

#Usage
info = get_service_info('falcon-sensor')
if info.get('active', True):
    print(f'sensor running with PID {info["pid"]}')
else:
    print('sensor not running')