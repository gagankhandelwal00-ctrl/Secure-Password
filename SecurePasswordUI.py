import tkinter as tk
from tkinter import messagebox

def generate_password():
    name = entry_name.get().strip()
    nickname = entry_nickname.get().strip()
    year = entry_year.get().strip()

    if not name or not nickname or not year:
        messagebox.showwarning("Missing Info", "Please fill in all fields.")
        return
    if len(name) < 3:
        messagebox.showwarning("Invalid", "Name must be at least 3 characters.")
        return
    if len(nickname) < 4:
        messagebox.showwarning("Invalid", "Nickname must be at least 4 characters.")
        return
    if len(year) != 4 or not year.isdigit():
        messagebox.showwarning("Invalid", "Birth year must be a 4-digit number.")
        return

    password = name[:3] + nickname[1:4] + year[::-1]
    result_var.set(password)

def copy_password():
    pwd = result_var.get()
    if pwd:
        root.clipboard_clear()
        root.clipboard_append(pwd)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title("Secure Password Generator")
root.geometry("400x320")
root.resizable(False, False)
root.configure(bg="#1e1e2e")

FONT = ("Segoe UI", 11)
BG = "#1e1e2e"
FG = "#cdd6f4"
ENTRY_BG = "#313244"
BTN_BG = "#89b4fa"
BTN_FG = "#1e1e2e"

tk.Label(root, text="🔐 Secure Password Generator", font=("Segoe UI", 14, "bold"), bg=BG, fg=BTN_BG).pack(pady=(18, 10))

frame = tk.Frame(root, bg=BG)
frame.pack(padx=30, fill="x")

tk.Label(frame, text="Your Name:", font=FONT, bg=BG, fg=FG, anchor="w").pack(fill="x", pady=(8, 0))
entry_name = tk.Entry(frame, font=FONT, bg=ENTRY_BG, fg=FG, insertbackground=FG, relief="flat", bd=5)
entry_name.pack(fill="x")

tk.Label(frame, text="Nickname:", font=FONT, bg=BG, fg=FG, anchor="w").pack(fill="x", pady=(8, 0))
entry_nickname = tk.Entry(frame, font=FONT, bg=ENTRY_BG, fg=FG, insertbackground=FG, relief="flat", bd=5)
entry_nickname.pack(fill="x")

tk.Label(frame, text="Birth Year:", font=FONT, bg=BG, fg=FG, anchor="w").pack(fill="x", pady=(8, 0))
entry_year = tk.Entry(frame, font=FONT, bg=ENTRY_BG, fg=FG, insertbackground=FG, relief="flat", bd=5)
entry_year.pack(fill="x")

tk.Button(root, text="Generate Password", font=("Segoe UI", 11, "bold"), bg=BTN_BG, fg=BTN_FG,
          relief="flat", cursor="hand2", command=generate_password).pack(pady=(18, 6), ipadx=10, ipady=4)

result_var = tk.StringVar()
result_entry = tk.Entry(root, textvariable=result_var, font=("Segoe UI", 12, "bold"), bg=ENTRY_BG,
                        fg="#a6e3a1", insertbackground=FG, relief="flat", bd=5, justify="center", state="readonly")
result_entry.pack(padx=30, fill="x")

tk.Button(root, text="Copy", font=FONT, bg="#585b70", fg=FG, relief="flat",
          cursor="hand2", command=copy_password).pack(pady=(6, 0), ipadx=14, ipady=2)

root.mainloop()
