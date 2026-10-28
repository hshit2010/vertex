import socket
from pynput import keyboard, mouse

testing = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
is_active = False 
is_connected = False
move_counter = 0
recent_actions = ["Awaiting connection..."]

def log_action(action_str):
    global recent_actions
    recent_actions.append(action_str)
    if len(recent_actions) > 5:
        recent_actions.pop(0)

def connect_server(target_ip):
    global is_connected
    try:
        testing.connect((target_ip, 9999))
        is_connected = True
        log_action(f"Connected to {target_ip}")
        return True
    except Exception:
        log_action("Connection failed.")
        return False

def on_press(key):
    global is_active
    if key == keyboard.Key.f12:
        is_active = not is_active
        return      
    
    if is_active and is_connected:
        log_action(f"Key Pressed: {key}")
        try:
            testing.send(f"{key}\n".encode())
        except Exception:
            pass

def on_move(x, y):
    global move_counter
    if is_active and is_connected:
        move_counter += 1
        if move_counter % 5 == 0:  
            try:
                testing.send(f"MOUSE_MOVE:{x},{y}\n".encode())
            except Exception:
                pass

def on_click(x, y, button, pressed):
    if is_active and is_connected and pressed:
        log_action(f"Clicked: {button}")
        try:
            testing.send(f"MOUSE_CLICK:{button}\n".encode()) 
        except Exception:
            pass

def on_scroll(x, y, dx, dy):
    if is_active and is_connected:
        log_action(f"Scrolled: {dy}")
        try:
            testing.send(f"MOUSE_SCROLL:{dx},{dy}\n".encode())
        except Exception:
            pass

keyboard_listener = keyboard.Listener(on_press=on_press)
mouse_listener = mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)

keyboard_listener.start()
mouse_listener.start()
