import tkinter as tk
from tkinter import messagebox

def proses_pilihan():
    pilihan = entry_pilihan.get().strip()
    if pilihan == "1":
        messagebox.showinfo("Info", "Keren! Semangat kuliahnya 💪")
    elif pilihan == "2":
        messagebox.showinfo("Info", "Mantap! Semoga dapet pekerjaan yang terbaik 🙌")
    else:
        messagebox.showerror("Error", "Pilihan tidak valid.")

root = tk.Tk()
root.title("Rencana Setelah Lulus Sekolah")
root.geometry("300x180")

label = tk.Label(root, text="Rencana setelah lulus sekolah?\n1. Kuliah\n2. Kerja")
label.pack(pady=10)

entry_pilihan = tk.Entry(root)
entry_pilihan.pack(pady=5)

btn_submit = tk.Button(root, text="Submit", command=proses_pilihan)
btn_submit.pack(pady=10)

root.mainloop()
