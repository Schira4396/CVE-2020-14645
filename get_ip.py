import socket


def get_network_ip():
    """get the local network ip, not loopback 127.*"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('192.168.254.5',80))
    ip = s.getsockname()[0]
    s.close()
    return ip



ipaddr = get_network_ip()
print(ipaddr)
