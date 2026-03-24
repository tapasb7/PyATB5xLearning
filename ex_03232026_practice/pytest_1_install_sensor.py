# "You have 50 Linux servers.
# Write Python to install the EDR sensor on each,
# track success/failure, and return a summary report."

import subprocess
from datetime import datetime

def install_sensor_multiple_server(servers,installer_path):
    report = {
        'total' : len(servers),
        'success' : [],
        'failure' : [],
        'timestamp' : datetime.now().isoformat()
    }

    for server in servers:
        try:
            result = subprocess.run(
                ['ssh', server, 'sudo dpkg -i', installer_path],
                capture_output=True,
                check=True,
                timeout=120

            )
            if result.returncode == 0:
                report['success'].append({'server':server,'output':result.stdout})
            else:
                report['failure'].append({'server':server,'reason':result.stderr})
        except subprocess.TimeoutExpired:
            report['failure'].append({'server':server,'reason':'timeout'})
        except Exception as e:
            report['failure'].append({'server':server,'reason':str(e)})


    report['success_count'] = len(report['success'])
    report['failure_count'] = len(report['failure'])
    return report