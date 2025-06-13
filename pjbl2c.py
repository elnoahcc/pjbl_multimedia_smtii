import tkinter as tk

def konversi():
    try:
        k = float(entry.get())
        c = k - 273
        r = (4/5) * (k - 273)
        f = (9/5) * (k - 273) + 32
        hasil.set(f"Celcius: {c:.2f}°C\nReamur: {r:.2f}°R\nFahrenheit: {f:.2f}°F")
    except:
        hasil.set("Masukkan angka yang valid!")

root = tk.Tk()
root.title("Konversi Kelvin")

tk.Label(root, text="Masukkan suhu dalam Kelvin:").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Konversi", command=konversi).pack(pady=5)

hasil = tk.StringVar()
tk.Label(root, textvariable=hasil).pack()

root.mainloop()
