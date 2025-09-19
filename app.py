
import tkinter as tk
from tkinter import ttk
import sqlite3

# ---------- Database Setup ----------
conn = sqlite3.connect("appointments.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        date TEXT,
        time TEXT,
        service TEXT
    )
""")
conn.commit()

# ---------- Tkinter UI ----------
root = tk.Tk()
root.title("Appointment Manager")
root.geometry("800x600")
root.configure(bg="#e6f7ff")

tk.Label(root, text="Appointment Manager", font=("Arial", 18, "bold"), bg="#e6f7ff").pack(pady=10)

# Input Form
form_frame = tk.Frame(root, bg="#e6f7ff")
form_frame.pack(pady=20)

tk.Label(form_frame, text="Name:", bg="#e6f7ff").grid(row=0, column=0, padx=10, pady=5, sticky="w")
name_entry = tk.Entry(form_frame, width=40)
name_entry.grid(row=0, column=1)

tk.Label(form_frame, text="Date (YYYY-MM-DD):", bg="#e6f7ff").grid(row=1, column=0, padx=10, pady=5, sticky="w")
date_entry = tk.Entry(form_frame, width=40)
date_entry.grid(row=1, column=1)

tk.Label(form_frame, text="Time (HH:MM):", bg="#e6f7ff").grid(row=2, column=0, padx=10, pady=5, sticky="w")
time_entry = tk.Entry(form_frame, width=40)
time_entry.grid(row=2, column=1)

tk.Label(form_frame, text="Service:", bg="#e6f7ff").grid(row=3, column=0, padx=10, pady=5, sticky="w")
service_entry = tk.Entry(form_frame, width=40)
service_entry.grid(row=3, column=1)


# ---------- Functions ----------
def add_appointment():
    name = name_entry.get()
    date = date_entry.get()
    time = time_entry.get()
    service = service_entry.get()

    if name and date and time and service:
        cursor.execute("INSERT INTO appointments (name, date, time, service) VALUES (?, ?, ?, ?)",
                       (name, date, time, service))
        conn.commit()
        view_appointments()
        clear_inputs()

def view_appointments():
    # clear table first
    for row in appointment_table.get_children():
        appointment_table.delete(row)

    cursor.execute("SELECT * FROM appointments")
    for row in cursor.fetchall():
        appointment_table.insert("", "end", values=row)

def clear_inputs():
    name_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)
    service_entry.delete(0, tk.END)

def delete_appointment():
    selected = appointment_table.selection()
    if selected:
        item = appointment_table.item(selected[0])
        record_id = item['values'][0]
        cursor.execute("DELETE FROM appointments WHERE id=?", (record_id,))
        conn.commit()
        view_appointments()


# ---------- Buttons ----------
button_frame = tk.Frame(root, bg="#e6f7ff")
button_frame.pack(pady=20)

tk.Button(button_frame, text="Add", width=20, bg="#4CAF50", fg="white", command=add_appointment).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="View", width=20, bg="#2196F3", fg="white", command=view_appointments).grid(row=0, column=1, padx=10)
tk.Button(button_frame, text="Delete", width=20, bg="#F44336", fg="white", command=delete_appointment).grid(row=0, column=2, padx=10)

# ---------- Table ----------
table_frame = tk.Frame(root, bg="#e6f7ff")
table_frame.pack(pady=20)

columns = ("ID", "Name", "Date", "Time", "Service")
appointment_table = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)

for col in columns:
    appointment_table.heading(col, text=col)
    appointment_table.column(col, width=120)

appointment_table.pack()

# Run the app
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
