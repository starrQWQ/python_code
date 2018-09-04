import socket

c=socket.socket()

host=socket.gethostname()
port=1000

c.connect((host,port))
print c.recv(1024)