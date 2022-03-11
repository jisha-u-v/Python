# server.py
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #af_inet for ipv4  and sock_stream is for TCP socket
s.bind((socket.gethostname(),1234)) #binding socket to port on the server 
s.listen(3) #listen for incoming connection in queue of 3
while True:
    clientsocket,addr=s.accept()
    print(f"connection from {addr}")
    clientsocket.send(bytes("Welcome to UST",'utf-8'))