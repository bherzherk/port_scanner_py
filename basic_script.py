#!/usr/bin/env python3
import socket

host = '192.168.68.1' # gateway IP
port = 80

def port_scanner(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1) # wait time to connect

    if s.connect_ex((host, port)) == 0:
        print(f"\n[+] The port {port} is opened.")
    else:
        print(f"\n[+] The port {port} is closed")

def run_scanner():
    port_scanner(port)

if __name__ == "__main__":
    run_scanner()
