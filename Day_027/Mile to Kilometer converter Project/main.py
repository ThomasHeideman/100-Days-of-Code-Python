from ctypes import windll
from tkinter import *

try:
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

# region functions
def calc():
    try:
        label_conversion["text"] = f"{float(input_field.get()) * 1.609344:.2f}"
    except ValueError:
        label_conversion["text"] = "0"
# endregion

#  region Window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=350)
window.config(padx=50, pady=40, background="#e9eef6")


window.columnconfigure(0, weight=1, uniform="equal")
window.columnconfigure(1, weight=1, uniform="equal")
window.columnconfigure(2, weight=1, uniform="equal")
window.iconbitmap("favicon.ico")
# endregion

# region UI elements
title = Label(text="Mile to Km Converter", font=("Segoe UI", 18, "bold"), background="#e9eef6", fg="#222340")
title.grid(row=0, column=0, columnspan=3, pady=(0, 30))


input_field = Entry(width=10, font=("Segoe UI", 14), relief="flat", justify="center")
input_field.grid(row=1, column=1, pady=24)

label_miles = Label(text="Miles", font=("Segoe UI", 14), background="#e9eef6", fg="#222340")
label_miles.grid(row=1, column=2, sticky="w", padx=16)


label_equal = Label(text="is equal to", font=("Segoe UI", 14), background="#e9eef6", fg="#222340")
label_equal.grid(row=2, column=0, sticky="e", padx=16)

label_conversion = Label(text="0", font=("Segoe UI", 16, "bold"), background="#e9eef6", fg="#222340")
label_conversion.grid(row=2, column=1, pady=10)

label_km = Label(text="Kilometer", font=("Segoe UI", 14), background="#e9eef6", fg="#222340")
label_km.grid(row=2, column=2, sticky="w", padx=16)


button = Button(text="Convert", font=("Segoe UI", 12, "bold"), command=calc, relief="flat", cursor="hand2")
button.config(fg="white", bg="#222340", activeforeground="white", activebackground="#383953", width=12, pady=6)
button.grid(row=3, column=1, pady=32)
# endregion

window.mainloop()