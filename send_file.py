import socket  # Import socket module

s = socket.socket()  # Create a socket object
host = "192.168.1.2"  # Get local machine name
port = 58012  # Reserve a port for your service.

s.connect((host, port))
#s.send(b"Hello server!")
f = open('out_text.txt', 'rb')
print('Sending...')
l = f.read(1024)
while l:
    print('Sending...')
    s.send(l)
    l = f.read(1024)
f.close()
print("Done Sending")
s.shutdown(socket.SHUT_WR)
print(s.recv(1024))
s.close()
