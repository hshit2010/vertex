import socket
from pynput import keyboard, mouse



keyboard_typer = keyboard.Controller()
mouse_controller=mouse.Controller()

receiver = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
receiver.bind(("0.0.0.0",9999))
receiver.listen( )
conn, addr = receiver.accept()
while True:
    message = conn.recv(1024).decode()
    if not message:
        break
    try:
        if message.startswith("MOUSE_MOVE: "):
            coords=message.split(":")[1]
            x, y =coords.split(",")
            mouse_controller.position = (float(x), float(y))
        elif message.startswith("MOUSE_CLICK:"):
            btn_str = message.split(":")[1]
            btn_name = btn_str.split(".")[1]
            button = getattr(mouse.Button, btn_name)
            mouse_controller.press(button)
            mouse_controller.release(button)
        elif message.startswith("MOUSE_SCROLL:"):
            scroll_data = message.split(":")[1]
            dx, dy = scroll_data.split(",")
            mouse_controller.scroll(float(dx), float(dy))
        else:
            clean_key = message.replace("'","")

            if clean_key.startswith("key."):
                key_name = clean_key.split(".")[1]
                special_key= getattr(keyboard.key, key_name)
                keyboard_typer.press(special_key)
                keyboard_typer.release(special_key)
            else:
                keyboard_typer.press(clean_key)
                keyboard_typer.release(clean_key)
    except Exception as e:
        print(f"slkipping comman: {message} | Error: {e}")
