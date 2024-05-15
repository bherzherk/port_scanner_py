#!/usr/bin/env python3
import socket
import argparse
from concurrent.futures import ThreadPoolExecutor
from termcolor import colored

def get_arguments():
    parser = argparse.ArgumentParser(description="Fast TCP Port Scanner")
    parser.add_argument("-t", "--target", dest="target", required=True, help="Target IP address to scan.")
    parser.add_argument("-p", "--port", dest="port", required=True, help="Port range (port-port) / port set (<port1>, <port2>, ...) / port")
    options = parser.parse_args()

    return options.target, options.port

def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    return s

def port_scanner(port, host):
    s = create_socket()

    try:
        s.connect((host, port))
        print(colored(f"\n[+] The port {port} is open.", 'cyan'))
    except (socket.timeout, ConnectionRefusedError):
        pass
    finally:
        s.close()

def thread_exe(ports, target):
    with ThreadPoolExecutor(max_workers=80) as executor:
        executor.map(lambda port: port_scanner(port, target), ports)

def parse_ports(ports_str):
    if '-' in ports_str:
        start, end = map(int, ports_str.split('-'))
        return range(start, end+1)
    elif ',' in ports_str:
        return map(int, ports_str.split(','))
    else:
        return (int(ports_str),)

def run_scanner():
    target, ports_str = get_arguments()
    ports = parse_ports(ports_str)
    thread_exe(ports, target)

if __name__ == "__main__":
    run_scanner()
