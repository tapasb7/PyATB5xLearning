#How do you test an API endpoint in Python?
# Write a complete test.

import requests

def test_alert_api(base_url, token):
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    try:
        r = requests.get(
            f'{base_url}/api/v1/alerts',
            headers=headers,
            timeout=10,
        )
        assert r.status_code == 200, f'Expected 200, got {r.status_code}'

        #assert JSON stucture
        data = r.json()
        assert 'alerts' in data
        assert isinstance(data['alerts'], list)

        #validate each alert has required fields
        required = ['id','severity','src_type', 'timestamp']
        for alert in data['alerts']:
            for field in required:
                assert field in alert, f'Missing field {field}'

        return True, data
    except requests.Timeout:
        return False, 'API timed out'






