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
print('die')
import sqlite3
import tkinter as tk

def view_records():
    conn = sqlite3.connect("records.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM records")
    rows = cursor.fetchall()
    conn.close()

    listbox.delete(0, tk.END)
    for row in rows:
        listbox.insert(tk.END, f"ID:{row[0]} | {row[1]} - {row[2]}")

root = tk.Tk()
root.title("Record Manager")
root.geometry("700x600")
root.configure(bg="#e6f7ff")

listbox = tk.Listbox(root, width=60, height=10)
listbox.pack(pady=10)

btn_view = tk.Button(root, text="View Records", command=view_records, bg="#006600", fg="white")
btn_view.pack(pady=5)

print("✅ View function ready! Run part6_delete next.")
root.mainloop()

import sqlite3
import tkinter as tk

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

def add_record():
    title = entry_title.get()
    desc = entry_desc.get()

    if title.strip() == "":
        status_label.config(text="⚠️ Title cannot be empty!", fg="red")
        return

    conn = sqlite3.connect("records.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO records (title, description) VALUES (?, ?)", (title, desc))
    conn.commit()
    conn.close()

    entry_title.delete(0, tk.END)
    entry_desc.delete(0, tk.END)

    status_label.config(text="✅ Record added successfully!", fg="green")

root = tk.Tk()
root.title("Record Manager")
root.geometry("700x600")
root.configure(bg="#e6f7ff")

tk.Label(root, text="Title:", bg="#e6f7ff").pack()
entry_title = tk.Entry(root, width=40)
entry_title.pack()

tk.Label(root, text="Description:", bg="#e6f7ff").pack()
entry_desc = tk.Entry(root, width=40)
entry_desc.pack()

btn_add = tk.Button(root, text="Add Record", command=add_record, bg="#0099cc", fg="white")
btn_add.pack(pady=5)

status_label = tk.Label(root, text="", bg="#e6f7ff")
status_label.pack()

init_db()
print("✅ Add function ready! Run part5_view next.")
root.mainloop()
