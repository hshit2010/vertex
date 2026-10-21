import socket
from pynput import keyboard

typer = keyboard.Controller()

receiver = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
receiver.bind(('0.0.0.0',9999))
receiver.listen( )
conn, addr = receiver.accept()
while True:
    message = conn.recv(1024).decode()
    clean_key = message.replace("'","")
    try:
        typer.press(clean_key)
        typer.release(clean_key)
    except ValueError:
        print(f"skipping special key: {message}")
