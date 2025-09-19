# final_record_manager.py
# Integrated Record Manager Application
import sqlite3
import tkinter as tk
from tkinter import messagebox

# ------------------ Database Setup (NSD) ------------------
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

# ------------------ Add Record Function (kyerewaa) ------------------
def add_record():
    title = entry_title.get()
    desc = entry_desc.get("1.0", tk.END).strip()  # Using Text widget now

    if title.strip() == "":
        status_label.config(text="⚠️ Title cannot be empty!", fg="red")
        return

    conn = sqlite3.connect("records.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO records (title, description) VALUES (?, ?)", (title, desc))
    conn.commit()
    conn.close()

    entry_title.delete(0, tk.END)
    entry_desc.delete("1.0", tk.END)
    view_records()  # Refresh the list automatically
    status_label.config(text="✅ Record added successfully!", fg="green")

# ------------------ View Records Function (Titus) ------------------
def view_records():
    conn = sqlite3.connect("records.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM records")
    rows = cursor.fetchall()
    conn.close()

    listbox.delete(0, tk.END)
    for row in rows:
        listbox.insert(tk.END, f"ID:{row[0]} | {row[1]} - {row[2]}")
    status_label.config(text="📋 Records loaded!", fg="blue")

# ------------------ Delete Record Function (Marcel) ------------------
def delete_record():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "⚠️ Please select a record to delete!")
        return
        
    confirmation = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this record?")
    if not confirmation:
        return
        
    record_text = listbox.get(selected[0])
    record_id = int(record_text.split("|")[0].replace("ID:", "").strip())

    conn = sqlite3.connect("records.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM records WHERE id=?", (record_id,))
    conn.commit()
    conn.close()

    view_records()
    status_label.config(text="🗑️ Record deleted!", fg="red")

# ------------------ Update Record Function (Obed) ------------------
def update_record():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "⚠️ Please select a record to update!")
        return
        
    record_text = listbox.get(selected[0])
    record_id = int(record_text.split("|")[0].replace("ID:", "").strip())

    new_title = entry_title.get()
    new_desc = entry_desc.get("1.0", tk.END).strip()

    if new_title.strip() == "":
        status_label.config(text="⚠️ Title cannot be empty!", fg="red")
        return

    conn = sqlite3.connect("records.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE records SET title=?, description=? WHERE id=?", (new_title, new_desc, record_id))
    conn.commit()
    conn.close()

    view_records()
    # Clear fields after update
    entry_title.delete(0, tk.END)
    entry_desc.delete("1.0", tk.END)
    status_label.config(text="✏️ Record updated successfully!", fg="blue")

# ------------------ Populate Fields for Editing ------------------
def on_select(event):
    try:
        selected = listbox.curselection()
        if selected:
            record_text = listbox.get(selected[0])
            parts = record_text.split("|")
            title = parts[1].split("-")[0].strip()
            desc = parts[1].split("-")[1].strip() if len(parts[1].split("-")) > 1 else ""
            
            # Populate the entry fields
            entry_title.delete(0, tk.END)
            entry_title.insert(0, title)
            
            entry_desc.delete("1.0", tk.END)
            entry_desc.insert("1.0", desc)
    except:
        pass  # Silently handle any errors during selection

# ------------------ GUI Setup (Blossom, Valary, sxj) ------------------
root = tk.Tk()
root.title("Record Manager")
root.geometry("700x600")
root.configure(bg="#e6f7ff")

# Title Label
title_label = tk.Label(root, text="🎨 Record Manager App", font=("Arial", 20, "bold"), bg="#e6f7ff", fg="#333")
title_label.pack(pady=10)

# Input Frame
input_frame = tk.Frame(root, bg="#e6f7ff")
input_frame.pack(pady=10)

tk.Label(input_frame, text="Title:", bg="#e6f7ff").grid(row=0, column=0, sticky='e', padx=5, pady=5)
entry_title = tk.Entry(input_frame, width=40, font=("Arial", 10))
entry_title.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Description:", bg="#e6f7ff").grid(row=1, column=0, sticky='e', padx=5, pady=5)
entry_desc = tk.Text(input_frame, width=40, height=4, font=("Arial", 10))
entry_desc.grid(row=1, column=1, padx=5, pady=5)

# Button Frame
button_frame = tk.Frame(root, bg="#e6f7ff")
button_frame.pack(pady=10)

btn_add = tk.Button(button_frame, text="Add Record", command=add_record, bg="#0099cc", fg="white", width=12)
btn_add.grid(row=0, column=0, padx=5)

btn_view = tk.Button(button_frame, text="View Records", command=view_records, bg="#006600", fg="white", width=12)
btn_view.grid(row=0, column=1, padx=5)

btn_update = tk.Button(button_frame, text="Update Record", command=update_record, bg="#ff9900", fg="white", width=12)
btn_update.grid(row=0, column=2, padx=5)

btn_delete = tk.Button(button_frame, text="Delete Record", command=delete_record, bg="#cc0000", fg="white", width=12)
btn_delete.grid(row=0, column=3, padx=5)

# Listbox with Scrollbar
list_frame = tk.Frame(root)
list_frame.pack(pady=10, fill=tk.BOTH, expand=True, padx=20)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(list_frame, width=80, height=15, yscrollcommand=scrollbar.set, font=("Courier", 10))
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=listbox.yview)

# Bind selection event
listbox.bind('<<ListboxSelect>>', on_select)

# Status Label
status_label = tk.Label(root, text="Welcome! Use the buttons to manage your records.", 
                       bg="#e6f7ff", fg="blue", font=("Arial", 10))
status_label.pack(pady=5)

# Initialize database and view
init_db()
view_records()

# Start the application
root.mainloop()
