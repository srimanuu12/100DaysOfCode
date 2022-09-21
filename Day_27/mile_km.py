from cgitb import text
from tkinter import *
FONT=("Arial", 10, "normal")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200,height=80)

mile = Label(text="Miles", font=FONT)
mile.grid(column=4,row=2)

km = Label(text="Km", font=FONT)
km.grid(column=4,row=3)

from_ = Label(text = "From:", font = FONT)
from_.grid(column=2, row=2)

to = Label(text = "To:", font = FONT)
to.grid(column=2, row=3)

mile_value = Entry(width=10)
mile_value.grid(column=3,row=2)

km_value = Label(text="0",width=10)
km_value.grid(column=3,row=3)

def convertion():
    miles = float(mile_value.get())
    kms = miles * 1.689
    km_value.config(text=f"{kms}")

convert = Button(text="Convert", command = convertion, padx=1, pady=0.5)
convert.grid(column=3,row=4)

window.mainloop()