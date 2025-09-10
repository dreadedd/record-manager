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
print('dickhead')
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
