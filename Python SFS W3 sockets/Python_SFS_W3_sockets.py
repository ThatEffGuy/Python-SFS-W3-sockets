import socket
host = socket.gethostname()
port = 12345
s = socket.socket()
s.connect((host,port))
s.sendall(b'This will be sent to server')
data = s.recv(1024)
print(data)
s.close()
