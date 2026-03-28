import socket
import pytest

def test_port_is_open():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('192.168.1.10', 443))
    sock.close()
    assert result == 0, f"Port 443 is not open, error: {result}"


