import socket

testing = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
testing.connect(('localhost',9999))
testing.send("heyy".encode())
