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
