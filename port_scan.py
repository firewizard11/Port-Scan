import argparse
import socket
import threading


def test_port(host: str, port: int) -> None:
    if not validate_host(host):
        raise ValueError(f'Host is Invalid: {host}')
    
    if not validate_port(port):
        raise ValueError(f'Port is Invalid: {port}')

    print(f'[*] Testing Port {port} on {host}...')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)

        try:    
            sock.connect((host, port))
        except:
            print(f'[!] {port}: Connection Failure')
            return None
        
        print(f'[*] {port}: Connection Success')
        return None
    

def sequential_scan(host: str, ports: list[int]) -> None:
    print(f'[*] Starting Sequential Scan on {host}')

    for port in ports:
        test_port(host, port)


def threaded_scan(host: str, ports: list[int]) -> None:
    threads = []

    print(f'[*] Starting Threaded Scan on {host}')
    for port in ports:
        thread = threading.Thread(target=test_port, args=(host, port))
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


def format_ports(ports: str) -> list[int]:
    """ Formats various forms of port inputs into a list of port numbers 
    
    Supported Formats:
    - Single Port (e.g. "40" or "40000")
    - Range of Ports (Inclusive) (e.g. "40-2000")
    - List of Ports (e.g. 21,22,80,139,443,445)
    """
    # List of Ports 
    if ',' in ports:
        temp = ports.split(',')

        for elem in temp:
            if not elem.isdecimal():
                raise ValueError(f'Please Enter a list of valid ports: {elem}')
            
            if not validate_port(int(elem)):
                raise ValueError(f'Error: Invalid Port in List {elem}')
            
        return [int(port) for port in temp]
    
    # Range of Ports
    if '-' in ports:
        temp = ports.split('-')

        if len(temp) != 2:
            raise ValueError(f'Error: Incorrect Number of Ports in Range of Ports: {ports}')
        
        for elem in temp:
            if not elem.isdecimal():
                raise ValueError(f'Please Enter a Range of valid ports: {elem}')
            
            if not validate_port(int(elem)):
                raise ValueError(f'Error: Invalid Port in Range {elem}')
            
        start = int(temp[0])
        stop = int(temp[1]) + 1

        if start > stop:
            raise ValueError(f'{start} Should be smaller than {stop}')

        return list(range(start, stop))

    # Single Ports
    if not ports.isdecimal():
        raise ValueError(f'Use a Supported Port Format: {ports}')
    
    if not validate_port(int(ports)):
        raise ValueError(f'Enter a valid port: {ports}')
    
    return [int(ports)]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='port_scan.py'
    )

    scan_type = parser.add_mutually_exclusive_group()
    options = parser.add_argument_group()

    scan_type.add_argument('-t', '--threaded', action='store_true')
    scan_type.add_argument('-s', '--sequential', action='store_true')

    options.add_argument('-H', '--Host', required=True)
    options.add_argument('-P', '--Ports', required=True)

    args = parser.parse_args()

    sequential = args.sequential
    threaded = args.threaded

    if threaded is None and sequential is None:
        sequential = True

    host = args.Host

    if not validate_host(host):
        raise ValueError(f'Enter a Valid Host: {host}')

    ports = args.Ports

    f_ports = format_ports(ports)

    if sequential:
        sequential_scan(host, f_ports)
        exit()

    if threaded:
        threaded_scan(host, f_ports)
        exit()