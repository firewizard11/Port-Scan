import socket
import threading

HOST = '127.0.0.1'
PORTS = list(range(200, 500))


def test_port(host: str, port: int) -> None:
    print(f'[*] Testing Port {port} on {host}...')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)

        try:    
            sock.connect((host, port))
        except:
            print('[!] Connection Failure')
            return None
        
        print('[*] Connection Success')
        return None
    

def sequential_scan(ports: list[int]) -> None:
    for port in ports:
        test_port(port)


def threaded_scan(ports: list[int]) -> None:
    threads = []

    for port in ports:
        thread = threading.Thread(target=test_port, args=(port,))
        thread.start()

        threads.append(thread)

    for thread in threads:
        thread.join()


def validate_port(port: int) -> bool:
    return (1 <= port <= 65535)


def validate_host(host: str) -> bool:
    if '.' not in host or host.count('.') != 3:
        return False
    
    octets = host.split('.')

    if len(octets) != 4:
        return False
    
    for octet in octets:
        if not octet.isdecimal():
            return False

        if not (0 <= int(octet) <= 255):
            return False
        
        if int(octet) < 10 and len(octet) > 1:
            return False
        
        if int(octet) < 100 and len(octet) > 2:
            return False
        
        if int(octet) < 1000 and len(octet) > 3:
            return False
        
        if int(octet) < 10000 and len(octet) > 4:
            return False

    return True


if __name__ == '__main__':
    for port in PORTS:
        test_port(port)