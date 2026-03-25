import requests
import pytest

class TrellixAPIClient:
    def __init__(self, base_url, token):
        self.base_url = base_url,
        self.token = token,
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })
        self.session.verify = False #Test Env only

    def get_alerts(self, severity=None, limit=None):
        params = {'limit': limit}
        if severity:
            params['severity'] = severity
        r = self.session.get(f'{self.base_url}/vi/alerts', params=params, timeout=10)
        r.raise_for_status()
        return r.json()

    def block_ip(self, ip, reason):
        payload = {'ip': ip, 'reason': reason}
        r = self.session.post(f'{self.base_url}/vi/alerts',
                              json=payload, timeout=10)
        r.raise_for_status()
        return r.status_code == 201


    #Test using the client
    @pytest.fixture(scope="module")
    def api_client():
        return TrellixAPIClient("https://ndr-test.trellix.local", "test-token")

    def test_get_alerts_returns_list(api_client):
        data = api_client.get_alerts()
        assert "alerts" in data
        assert isinstance(data["alerts"], list)

    def test_critical_alerts_have_required_fields(api_client):
        data = api_client.get_alerts(severity="critical")
        required = ["id", "severity", "src_ip", "timestamp", "technique"]
        for alert in data["alerts"]:
            for field in required:
                assert field in alert, f"Alert {alert.get('id')} missing: {field}"

    @pytest.mark.parametrize("method,endpoint,expected_status", [
        ("GET", "/v1/health", 200),
        ("GET", "/v1/alerts", 200),
        ("GET", "/v1/invalid", 404),
    ])
    def test_api_endpoints_status(api_client, method, endpoint, expected_status):
        r = api_client.session.request(method, f"{api_client.base_url}{endpoint}", timeout=5)
        assert r.status_code == expected_status







