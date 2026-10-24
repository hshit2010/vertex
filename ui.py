import tkinter as tk
import main

root = tk.Tk()
root.title("Vertex KVM")
root.geometry("300x150")
root.configure(bg="#2b2b2b")

status_label = tk.Label(root, text = "KVM status: ACTIVE", fg="green", bg="#2b2b2b", font=("Arial", 14, "bold"))
status_label.pack(pady=40)
def check_status():
    if main.is_active:
        status_label.config(text="KVM status : ACTIVE", fg="green")
    else:
        status_label.config(text="KVM status: PAUSED", fg="red")

    root.after(100, check_status)

check_status()
root.mainloop()