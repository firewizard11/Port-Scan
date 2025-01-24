import socket

HOST = '127.0.0.1'
PORT = 4444

def test_port(host: str, port: int):
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
    

if __name__ == '__main__':
    test_port(HOST, PORT)