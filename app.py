import sqlite3

# ------------------ Database Setup ------------------
def init_db():
    conn = sqlite3.connect("records.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT
    )
    """)
    conn.commit()
    conn.close()

print("✅ Database setup complete! Run part2_window next.")
import tkinter as tk

root = tk.Tk()
root.title("Record Manager")
root.geometry("700x600")
root.configure(bg="#e6f7ff")

tk.Label(root, text="Record Manager App", font=("Arial", 18, "bold"), bg="#e6f7ff").pack(pady=10)

print("✅ Basic window created! Run part3_inputs next.")
root.mainloop()
import tkinter as tk

root = tk.Tk()
root.title("Record Manager")
root.geometry("700x600")
root.configure(bg="#e6f7ff")

# Title input
tk.Label(root, text="Title:", bg="#e6f7ff").pack()
entry_title = tk.Entry(root, width=40)
entry_title.pack()

# Description input
tk.Label(root, text="Description:", bg="#e6f7ff").pack()
entry_desc = tk.Entry(root, width=40)
entry_desc.pack()

print("✅ Input fields ready! Run part4_add next.")
root.mainloop()
