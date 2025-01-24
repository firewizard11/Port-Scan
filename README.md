# Port Scan

## Description

Port Scan is a Port Scanner written in Python

## Features

- CLI Interface
- Sequential Port Scan
- Multi-Threaded Port Scan
- Single Host Port Scan Only
- Supported Port Formats:
  - Single Port: "40", "50000", "1234"
  - Range of Ports (inclusive): "200-4000", "25000-50000", "1-65535"
  - List of Ports: "1, 1234, 4444, 80, 443"

## How To Use

### Example 1: Scan Port 200 to 4444 on 127.0.0.1 Sequentially

Command: python3 port_scan.py -H 127.0.0.1 -P 200-4444

### Example 2: Scan Port 21,22,80,139,443,445 on 182.141.0.21 Multi-Threaded(ly)

Command: python3 port_scan.py -H 182.141.0.21 -P 21,22,80,139,443,445 -t 
