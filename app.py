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

def delete_record():
    selected = listbox.curselection()
    if selected:
        record_text = listbox.get(selected[0])
        record_id = int(record_text.split("|")[0].replace("ID:", "").strip())

        conn = sqlite3.connect("records.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM records WHERE id=?", (record_id,))
        conn.commit()
        conn.close()

        view_records()
        status_label.config(text="🗑️ Record deleted!", fg="red")
    else:
        status_label.config(text="⚠️ Select a record to delete!", fg="red")

root = tk.Tk()
root.title("Record Manager")
root.geometry("700x600")
root.configure(bg="#e6f7ff")

listbox = tk.Listbox(root, width=60, height=10)
listbox.pack(pady=10)

btn_delete = tk.Button(root, text="Delete Record", command=delete_record, bg="#cc0000", fg="white")
btn_delete.pack(pady=5)

status_label = tk.Label(root, text="", bg="#e6f7ff")
status_label.pack()

print("✅ Delete function ready! Run part7_update next.")
root.mainloop()
import sqlite3
import tkinter as tk

def update_record():
    selected = listbox.curselection()
    if selected:
        record_text = listbox.get(selected[0])
        record_id = int(record_text.split("|")[0].replace("ID:", "").strip())

        new_title = entry_title.get()
        new_desc = entry_desc.get()

        conn = sqlite3.connect("records.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE records SET title=?, description=? WHERE id=?", (new_title, new_desc, record_id))
        conn.commit()
        conn.close()

        view_records()
        status_label.config(text="✏️ Record updated!", fg="blue")
    else:
        status_label.config(text="⚠️ Select a record to update!", fg="red")

root = tk.Tk()
root.title("Record Manager")
root.geometry("700x600")
root.configure(bg="#e6f7ff")

entry_title = tk.Entry(root, width=40)
entry_title.pack()

entry_desc = tk.Entry(root, width=40)
entry_desc.pack()

listbox = tk.Listbox(root, width=60, height=10)
listbox.pack(pady=10)

btn_update = tk.Button(root, text="Update Record", command=update_record, bg="#ff9900", fg="white")
btn_update.pack(pady=5)

status_label = tk.Label(root, text="", bg="#e6f7ff")
status_label.pack()

print("✅ Update function ready! Run part8_style next.")
root.mainloop()
import tkinter as tk

root = tk.Tk()
root.title("Record Manager")
root.geometry("700x600")
root.configure(bg="#e6f7ff")

tk.Label(root, text="🎨 Styled Record Manager App", font=("Arial", 20, "bold"), bg="#e6f7ff", fg="#333").pack(pady=10)
status_label = tk.Label(root, text="Welcome! All functions integrated!", bg="#e6f7ff", fg="blue")
status_label.pack()

print("✅ Styling done! Project complete.")
root.mainloop()
