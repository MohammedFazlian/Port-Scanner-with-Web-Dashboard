import socket
import threading

def scan_port(host, port, timeout=1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except socket.error:
        return False

def grab_banner(host, port, timeout=2):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((host, port))
        sock.send(b'HEAD / HTTP/1.0\r\n\r\n')
        banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
        sock.close()
        return banner[:200]
    except:
        return None

def resolve_host(host):
    try:
        ip = socket.gethostbyname(host)
        return ip
    except socket.gaierror:
        return None

def scan_range(host, start=1, end=1024):
    results = {}
    threads = []

    def check(port):
        is_open = scan_port(host, port)
        if is_open:
            banner = grab_banner(host, port)
            results[port] = {"open": True, "banner": banner}

    for port in range(start, end + 1):
        t = threading.Thread(target=lambda p=port: check(p))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return results