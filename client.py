import socket

while True:
    text_to_display = input("what do you want to display: ")
    testing = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    testing.connect(('localhost',9999))
    testing.send(text_to_display.encode())
