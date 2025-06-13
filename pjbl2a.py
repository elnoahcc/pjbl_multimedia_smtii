import tkinter as tk

def konversi():
    try:
        c = float(entry.get())
        r = (4/5) * c
        k = c + 273
        f = (9/5) * c + 32
        hasil.set(f"Reamur: {r:.2f}°R\nKelvin: {k:.2f}K\nFahrenheit: {f:.2f}°F")
    except:
        hasil.set("Masukkan angka yang valid!")

root = tk.Tk()
root.title("Konversi Celcius")

tk.Label(root, text="Masukkan suhu dalam Celcius:").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Konversi", command=konversi).pack(pady=5)

hasil = tk.StringVar()
tk.Label(root, textvariable=hasil).pack()

root.mainloop()
