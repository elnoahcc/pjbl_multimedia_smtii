import tkinter as tk

def konversi():
    try:
        f = float(entry.get())
        c = (5/9) * (f - 32)
        r = (4/9) * (f - 32)
        k = (5/9) * (f - 32) + 273
        hasil.set(f"Celcius: {c:.2f}°C\nReamur: {r:.2f}°R\nKelvin: {k:.2f}K")
    except:
        hasil.set("Masukkan angka yang valid!")

root = tk.Tk()
root.title("Konversi Fahrenheit")

tk.Label(root, text="Masukkan suhu dalam Fahrenheit:").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Konversi", command=konversi).pack(pady=5)

hasil = tk.StringVar()
tk.Label(root, textvariable=hasil).pack()

root.mainloop()
