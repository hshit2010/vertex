import tkinter as tk
import socket
import threading
import queue
from pynput import keyboard

PORT = 9999

typer = keyboard.Controller()
q = queue.Queue()

root = tk.Tk()
root.title("Vertex Server")
root.geometry("400x400")

status_label = tk.Label(root, text="Waiting...")
status_label.pack(pady=(15, 5))

received_box = tk.Text(root, height=18, width=45, state="disabled")
received_box.pack(pady=5)


def show(text):
    received_box.config(state="normal")
    received_box.insert(tk.END, text)
    received_box.see(tk.END)
    received_box.config(state="disabled")


def handle_key(k):
    if k in keyboard.Key.__members__:
        special_key = keyboard.Key[k]
        typer.press(special_key)
        typer.release(special_key)
        if k == "space":
            return " "
        if k == "enter":
            return "\n"
        return "[" + k + "]"
    if len(k) == 1:
        typer.press(k)
        typer.release(k)
        return k
    return ""


def run_server():
    receiver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    receiver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        receiver.bind(("0.0.0.0", PORT))
    except Exception:
        q.put(("status", "Could not start on port " + str(PORT)))
        return
    receiver.listen()
    while True:
        q.put(("status", "Waiting..."))
        conn, addr = receiver.accept()
        q.put(("status", "Connected to " + addr[0]))
        buffer = b""
        while True:
            try:
                data = conn.recv(1024)
            except Exception:
                break
            if not data:
                break
            buffer += data
            while b"\n" in buffer:
                line, buffer = buffer.split(b"\n", 1)
                k = line.decode(errors="ignore")
                if k == "":
                    continue
                try:
                    shown = handle_key(k)
                except Exception:
                    shown = ""
                if shown != "":
                    q.put(("key", shown))
        conn.close()


def check_queue():
    while not q.empty():
        kind, text = q.get()
        if kind == "status":
            status_label.config(text=text)
        elif kind == "key":
            show(text)
    root.after(100, check_queue)


thread = threading.Thread(target=run_server, daemon=True)
thread.start()
check_queue()
root.mainloop()
