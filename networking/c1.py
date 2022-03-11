# client.py
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))
msg=s.recv(1024)# receive data in buffer size of 1024 bytes
print(msg.decode('utf-8'))