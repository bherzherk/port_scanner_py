#!/usr/bin/env python3
import socket
import argparse
import sys 
from termcolor import colored

def get_arguments():
    parser = argparse.ArgumentParser(description="Fast TCP Port Scanner")
    parser.add_argument("-t", "--target", dest="target", help="Target IP (Ex. -t <ip-address> / --target <ip-address>)")
    parser.add_argument("-p", "--port", dest="port", help="Port range (ex. -p <port> / <port-range> / <port1, port2, ...>)")
    options = parser.parse_args()

    if options.target is None or options.port is None:
        parser.print_help()
        sys.exit(1)

    return options.target, options.port

def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    return s

def port_scanner(port, host):
    s = create_socket()
    try:
        s.connect((host, port))
        print(colored(f"\n[+] The port {port} is open", 'cyan'))
    except (socket.timeout, ConnectionRefusedError):
        pass
    finally:
        s.close()

def iter_ports(ports, target):
    for port in ports:
        port_scanner(port, target)

def parse_ports(ports_str):
    if '-' in ports_str:
        start, end = map(int, ports_str.split('-'))
        return range(start, end+1)
    elif ',' in ports_str:
        return map(int, ports_str.split(','))
    else:
        return (int(ports_str))

def run_scanner():
    target, ports_str = get_arguments()
    ports = parse_ports(ports_str)
    iter_ports(ports, target)

if __name__ == "__main__":
    run_scanner()
