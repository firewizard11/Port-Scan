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

if __name__ == '__main__':
    for port in PORTS:
        test_port(port)