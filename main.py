import tkinter as tk
import socket
import queue
from pynput import keyboard

PORT = 9999

sender = None
listener = None
q = queue.Queue()

root = tk.Tk()
root.title("Vertex Main")
root.geometry("400x450")

ip_label = tk.Label(root, text="Secondary laptop IP:")
ip_label.pack(pady=(15, 5))

ip_entry = tk.Entry(root, width=25)
ip_entry.pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

connect_button = tk.Button(button_frame, text="Connect", command=lambda: connect())
connect_button.pack(side="left", padx=5)

disconnect_button = tk.Button(button_frame, text="Disconnect", command=lambda: disconnect(), state="disabled")
disconnect_button.pack(side="left", padx=5)

status_label = tk.Label(root, text="Not connected")
status_label.pack(pady=10)

typed_label = tk.Label(root, text="What you typed:")
typed_label.pack()

typed_box = tk.Text(root, height=14, width=45, state="disabled")
typed_box.pack(pady=5)


def show(text):
    typed_box.config(state="normal")
    typed_box.insert(tk.END, text)
    typed_box.see(tk.END)
    typed_box.config(state="disabled")


def on_press(key):
    global sender
    if sender is None:
        return
    if hasattr(key, "char") and key.char:
        name = key.char
        shown = key.char
    elif hasattr(key, "name") and key.name:
        name = key.name
        if key.name == "space":
            shown = " "
        elif key.name == "enter":
            shown = "\n"
        else:
            shown = "[" + key.name + "]"
    else:
        return
    try:
        sender.send((name + "\n").encode())
        q.put(("key", shown))
    except Exception:
        q.put(("lost", ""))


def connect():
    global sender, listener
    ip = ip_entry.get().strip()
    if ip == "":
        status_label.config(text="Enter an IP first")
        return
    status_label.config(text="Connecting...")
    root.update()
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        s.connect((ip, PORT))
        s.settimeout(None)
    except Exception:
        status_label.config(text="Could not connect")
        return
    sender = s
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    status_label.config(text="Connected to " + ip)
    connect_button.config(state="disabled")
    disconnect_button.config(state="normal")


def disconnect():
    global sender, listener
    if listener is not None:
        listener.stop()
        listener = None
    if sender is not None:
        try:
            sender.close()
        except Exception:
            pass
        sender = None
    status_label.config(text="Not connected")
    connect_button.config(state="normal")
    disconnect_button.config(state="disabled")


def check_queue():
    while not q.empty():
        kind, text = q.get()
        if kind == "key":
            show(text)
        elif kind == "lost":
            if sender is not None:
                disconnect()
                status_label.config(text="Connection lost")
    root.after(100, check_queue)


def on_close():
    disconnect()
    root.destroy()


root.protocol("WM_DELETE_WINDOW", on_close)
check_queue()
root.mainloop()
