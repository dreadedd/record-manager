import tkinter as tk

root = tk.Tk()
root.title("Record Manager")
root.geometry("600x500")  # Enlarged window
root.configure(bg="#e6f7ff")

tk.Label(root, text="Record Manager App", font=("Arial", 18, "bold"), bg="#e6f7ff").pack(pady=10)

root.mainloop()

