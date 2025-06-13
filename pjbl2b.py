import tkinter as tk

def konversi():
    try:
        r = float(entry.get())
        c = (5/4) * r
        k = (5/4) * r + 273
        f = (9/4) * r + 32
        hasil.set(f"Celcius: {c:.2f}°C\nKelvin: {k:.2f}K\nFahrenheit: {f:.2f}°F")
    except:
        hasil.set("Masukkan angka yang valid!")

root = tk.Tk()
root.title("Konversi Reamur")

tk.Label(root, text="Masukkan suhu dalam Reamur:").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Konversi", command=konversi).pack(pady=5)

hasil = tk.StringVar()
tk.Label(root, textvariable=hasil).pack()

root.mainloop()
