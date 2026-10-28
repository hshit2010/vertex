import tkinter as tk
import main

root = tk.Tk()
root.title("Vertex KVM Control Panel")
root.geometry("400x400")
root.configure(bg="#1e1e1e")

header = tk.Label(root, text="Vertex KVM System", fg="#00aaff", bg="#1e1e1e", font=("Arial", 16, "bold"))
header.pack(pady=(20, 5))

ip_frame = tk.Frame(root, bg="#1e1e1e")
ip_frame.pack(pady=10)

ip_label = tk.Label(ip_frame, text="Linux IP:", fg="#a0a0a0", bg="#1e1e1e", font=("Arial", 10))
ip_label.pack(side="left", padx=5)

ip_entry = tk.Entry(ip_frame, bg="#333333", fg="white", font=("Arial", 10), insertbackground="white", width=15)
ip_entry.pack(side="left", padx=5)

def try_connect():
    ip = ip_entry.get()
    if main.connect_server(ip):
        connect_btn.config(text="Connected", state="disabled", bg="green")
    else:
        connect_btn.config(text="Retry", bg="red")

connect_btn = tk.Button(ip_frame, text="Connect", bg="#00aaff", fg="white", command=try_connect, relief="flat", padx=10)
connect_btn.pack(side="left", padx=5)

status_label = tk.Label(root, text="KVM Status: DISCONNECTED", fg="orange", bg="#1e1e1e", font=("Arial", 14, "bold"))
status_label.pack(pady=10)

history_box = tk.Listbox(root, bg="#0d0d0d", fg="#00ff00", font=("Consolas", 11), height=6, highlightthickness=1, highlightbackground="#333333", borderwidth=0)
history_box.pack(fill="x", padx=25, pady=10)

def update_ui():
    if main.is_active and main.is_connected:
        status_label.config(text="KVM Status: ACTIVE", fg="#00ff00")
    elif not main.is_connected:
        status_label.config(text="KVM Status: DISCONNECTED", fg="orange")
    else:
        status_label.config(text="KVM Status: PAUSED", fg="red")
    
    history_box.delete(0, tk.END)
    for action in main.recent_actions:
        history_box.insert(tk.END, f"> {action}")
    
    root.after(100, update_ui)

update_ui()
root.mainloop()
