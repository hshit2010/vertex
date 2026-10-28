import socket
from pynput import keyboard

typer = keyboard.Controller()

receiver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
receiver.bind(("0.0.0.0", 9999))
receiver.listen()
print("Listening for keys on port 9999...")

conn, addr = receiver.accept()
print(f"Connected to {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
        
    keys = data.split('\n')
    for k in keys:
        if not k:
            continue
            
        try:
            # Type special keys (enter, space, etc.) or normal alphabets
            if hasattr(keyboard.Key, k):
                special_key = getattr(keyboard.Key, k)
                typer.press(special_key)
                typer.release(special_key)
            else:
                typer.press(k)
                typer.release(k)
        except Exception as e:
            pass
