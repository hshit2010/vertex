import socket

receiver = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
receiver.bind(('localhost',9999))
receiver.listen()
conn,addr = receiver.accept()
message = conn.recv(1024).decode()
print(message)
