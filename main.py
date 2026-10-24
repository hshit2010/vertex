import os
from dotenv import load_dotenv
from pynput import keyboard, mouse
import socket

load_dotenv()
server_ip = os.getenv("TARGET_IP")

testing = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
testing.connect(("localhost",9999))

is_active = False
move_counter = 0

recent_actions = ["Awaiting input...."]

def log_action(action_str):
	global recent_actions
	recent_actions.append(action_str)
	if len(recent_actions)>5:
		recent_actions.pop(0)

def on_press(key):
	global is_active
	
	
	if key == keyboard.Key.f12:
		is_active = not is_active
		print(f"KVM Active Status: {is_active}")
		return		
	
	if is_active:
		log_action(f"Key Pressed:{key}")
		print(key)
		try:
			testing.send(str(key).encode())
		except Exception as e:
			print(f"Connection error: {e}")
			return False

def on_move(x,y):
	if is_active:
		try:
			testing.send(f"MOUSE_MOVE:{x},{y}".encode())
		except Exception as e:
			print(f"Mouse move error: {e}")
def on_click(x,y, button, pressed):
	if is_active and pressed:
		log_action(f"clicked:{button}")
		try:
			testing.send(f"MOUSE_CLICK: {button}".encode())
		except Exception as e:
			print(f"Mouse click error: {e}")
def on_scroll(x, y, dx, dy):
	if is_active:
		log_action(f"scrolled:{dy}")
		try:
			testing.send(f"MOUSE_SCROLL:{dx},{dy}".encode())
		except Exception as e:
			pass
keyboard_listener = keyboard.Listener(on_press = on_press)
mouse_listener = mouse.Listener(on_move=on_move, on_click=on_click)

keyboard_listener.start()
mouse_listener.start()



			

