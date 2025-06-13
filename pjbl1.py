import tkinter as tk
from tkinter import messagebox

def hitung():
    try:
        angka1 = float(entry_angka1.get())
        angka2 = float(entry_angka2.get())
        operasi = pilihan.get()

        if operasi == "1. Penjumlahan":
            hasil = angka1 + angka2
            simbol = "+"
        elif operasi == "2. Pengurangan":
            hasil = angka1 - angka2
            simbol = "-"
        elif operasi == "3. Perkalian":
            hasil = angka1 * angka2
            simbol = "×"
        elif operasi == "4. Pembagian":
            if angka2 == 0:
                messagebox.showerror("Error", "Tidak bisa dibagi dengan nol!")
                return
            hasil = angka1 / angka2
            simbol = "÷"
        else:
            messagebox.showerror("Error", "Pilih operasi terlebih dahulu!")
            return

        # Format hasil untuk menampilkan desimal yang lebih rapi
        if hasil == int(hasil):
            hasil_tampil = int(hasil)
        else:
            hasil_tampil = round(hasil, 6)

        output_label.config(
            text=f"{angka1} {simbol} {angka2} = {hasil_tampil}",
            fg="blue"
        )
        lanjutkan_button.config(state=tk.NORMAL)

    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")

def lanjutkan():
    jawaban = lanjut_entry.get().strip().lower()
    if jawaban == "tidak":
        if messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin keluar?"):
            root.destroy()
    elif jawaban == "ya":
        # Reset semua input dan output
        entry_angka1.delete(0, tk.END)
        entry_angka2.delete(0, tk.END)
        output_label.config(text="", fg="black")
        lanjut_entry.delete(0, tk.END)
        lanjutkan_button.config(state=tk.DISABLED)
        pilihan.set(opsi[0])  # Reset pilihan ke default
        entry_angka1.focus()  # Focus ke input pertama
    else:
        messagebox.showwarning("Peringatan", "Silakan ketik 'ya' atau 'tidak'!")

def on_enter_pressed(event):
    """Fungsi untuk menjalankan perhitungan saat Enter ditekan"""
    hitung()

def on_continue_enter(event):
    """Fungsi untuk lanjutkan saat Enter ditekan di field lanjut"""
    lanjutkan()

# GUI Setup
root = tk.Tk()
root.title("🧮 Kalkulator Sederhana")
root.geometry("450x400")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# Frame utama
main_frame = tk.Frame(root, bg="#f0f0f0")
main_frame.pack(expand=True, fill='both', padx=20, pady=20)

# Judul
title_label = tk.Label(
    main_frame, 
    text="🧮 KALKULATOR SEDERHANA", 
    font=("Arial", 16, "bold"),
    bg="#f0f0f0",
    fg="#2c3e50"
)
title_label.pack(pady=(0, 20))

# Pilihan operasi
tk.Label(
    main_frame, 
    text="Pilih Operasi:", 
    font=("Arial", 11, "bold"),
    bg="#f0f0f0"
).pack(pady=(0, 5))

opsi = [
    "1. Penjumlahan",
    "2. Pengurangan", 
    "3. Perkalian",
    "4. Pembagian"
]

pilihan = tk.StringVar()
pilihan.set(opsi[0])

option_menu = tk.OptionMenu(main_frame, pilihan, *opsi)
option_menu.config(
    font=("Arial", 10),
    bg="white",
    width=15
)
option_menu.pack(pady=(0, 15))

# Input angka pertama
tk.Label(
    main_frame, 
    text="Masukkan angka pertama:", 
    font=("Arial", 10),
    bg="#f0f0f0"
).pack(pady=(0, 5))

entry_angka1 = tk.Entry(
    main_frame, 
    font=("Arial", 12),
    justify='center',
    width=20
)
entry_angka1.pack(pady=(0, 10))
entry_angka1.bind('<Return>', on_enter_pressed)  # Bind Enter key

# Input angka kedua
tk.Label(
    main_frame, 
    text="Masukkan angka kedua:", 
    font=("Arial", 10),
    bg="#f0f0f0"
).pack(pady=(0, 5))

entry_angka2 = tk.Entry(
    main_frame, 
    font=("Arial", 12),
    justify='center',
    width=20
)
entry_angka2.pack(pady=(0, 15))
entry_angka2.bind('<Return>', on_enter_pressed)  # Bind Enter key

# Tombol hitung
hitung_button = tk.Button(
    main_frame, 
    text="🔢 HITUNG", 
    command=hitung,
    bg="blue",
    fg="white",
    font=("Arial", 11, "bold"),
    padx=20,
    pady=5,
    cursor="hand2"
)
hitung_button.pack(pady=(0, 20))

# Output hasil
output_label = tk.Label(
    main_frame, 
    text="", 
    font=("Arial", 14, "bold"),
    bg="#f0f0f0",
    fg="#2c3e50"
)
output_label.pack(pady=(0, 20))

# Separator line
separator = tk.Frame(main_frame, height=2, bg="#bdc3c7")
separator.pack(fill='x', pady=(0, 15))

# Lanjutkan section
tk.Label(
    main_frame, 
    text="Lakukan perhitungan lagi? (ya/tidak):", 
    font=("Arial", 10),
    bg="#f0f0f0"
).pack(pady=(0, 5))

lanjut_entry = tk.Entry(
    main_frame, 
    font=("Arial", 11),
    justify='center',
    width=15
)
lanjut_entry.pack(pady=(0, 10))
lanjut_entry.bind('<Return>', on_continue_enter)  # Bind Enter key

lanjutkan_button = tk.Button(
    main_frame, 
    text="➡️ LANJUTKAN", 
    command=lanjutkan,
    bg="#3498db",
    fg="white",
    font=("Arial", 10, "bold"),
    state=tk.DISABLED,
    cursor="hand2"
)
lanjutkan_button.pack(pady=(0, 10))

# Focus awal ke input pertama
entry_angka1.focus()

# Jalankan aplikasi
root.mainloop()