from pynput import keyboard

def print_the_key(key):
    print(key)

listener = keyboard.Listener(on_press=print_the_key)
listener.start()
listener.join()