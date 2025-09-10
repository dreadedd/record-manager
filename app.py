import sqlite3
import tkinter as tk

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


# ------------------ Functions ------------------
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
    view_records()


def view_records():
    conn = sqlite3.connect("records.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM records")
    rows = cursor.fetchall()
    conn.close()

    listbox.delete(0, tk.END)
    for row in rows:
        listbox.insert(tk.END, f"ID:{row[0]} | {row[1]} - {row[2]}")


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


def update_record():
    selected = listbox.curselection()
    if selected:
        record_text = listbox.get(selected[0])
        record_id = int(record_text.split("|")[0].replace("ID:", "").strip())

        new_title = entry_title.get()
        new_desc = entry_desc.get()

        if new_title.strip() == "":
            status_label.config(text="⚠️ Title cannot be empty!", fg="red")
            return

        conn = sqlite3.connect("records.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE records SET title=?, description=? WHERE id=?", (new_title, new_desc, record_id))
        conn.commit()
        conn.close()

        view_records()
        status_label.config(text="✏️ Record updated!", fg="blue")
    else:
        status_label.config(text="⚠️ Select a record to update!", fg="red")


# ------------------ GUI Setup ------------------
root = tk.Tk()
root.title("Record Manager")
root.geometry("700x600")
root.configure(bg="#e6f7ff")

tk.Label(root, text="🎨 Record Manager App", font=("Arial", 20, "bold"), bg="#e6f7ff", fg="#333").pack(pady=10)

# Inputs
tk.Label(root, text="Title:", bg="#e6f7ff").pack()
entry_title = tk.Entry(root, width=40)
entry_title.pack()

tk.Label(root, text="Description:", bg="#e6f7ff").pack()
entry_desc = tk.Entry(root, width=40)
entry_desc.pack()

# Buttons
tk.Button(root, text="Add Record", command=add_record, bg="#0099cc", fg="white").pack(pady=5)
tk.Button(root, text="View Records", command=view_records, bg="#006600", fg="white").pack(pady=5)
tk.Button(root, text="Delete Record", command=delete_record, bg="#cc0000", fg="white").pack(pady=5)
tk.Button(root, text="Update Record", command=update_record, bg="#ff9900", fg="white").pack(pady=5)

# Listbox
listbox = tk.Listbox(root, width=60, height=10)
listbox.pack(pady=10)

# Status
status_label = tk.Label(root, text="Welcome! Ready to manage records.", bg="#e6f7ff", fg="blue")
status_label.pack()

# ------------------ Run App ------------------
init_db()
view_records()  # show records at startup
root.mainloop()
