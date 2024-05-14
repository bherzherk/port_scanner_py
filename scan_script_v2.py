#!/usr/bin/env python3
import socket
from termcolor import colored

host = input("[+] Enter the IP address: ")
# setting port range
start_range_port = int(input("Ports from: "))
end_range_port = int(input("To: "))

def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1) # wait time
    return s

def port_scanner(port):
    s = create_socket()

    try:
        s.connect((host, port))
        print(colored(f"\n[+] The port {port} is open", 'blue'))
    except (socket.timeout, ConnectionRefusedError):
        pass
    finally:
        s.close()

def run_scanner():

    for port in range(start_range_port, end_range_port+1):
        port_scanner(port)

if __name__ == "__main__":
    run_scanner()
