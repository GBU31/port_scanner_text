import socket


def Scan(ip):
    ports = [443, 80, 8080, 8000, 3000, 445, 9050, 123, 21, 19, 23, 22, 8081]
    open_ports = []
    open_ports.clear()
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                s.connect((ip, port))
                open_ports.append(port)
        except:
            pass
    else:
        return open_ports