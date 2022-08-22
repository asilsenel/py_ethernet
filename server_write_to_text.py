import socket
import os
import platform
from tempfile import TemporaryDirectory
from pathlib import Path

HOST = "192.168.1.43"  # Standard loopback interface address (localhost)
PORT = 58152  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if data:
                with open('out_text.txt', 'w') as output_file:
                    output_file.write(data.decode("utf-8"))
                    print(data)
            elif not data:
                break
            conn.sendall(data)

