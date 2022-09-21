from tkinter import *

window = Tk()
window.title("First GUI program")
window.minsize(width= 500, height= 600)
#padding for entire window
#if you want for particular button, entry,etc. you can use same like below
window.config(padx=100,pady=100)

# Label
my_label = Label(text = "Old Text", font = ("Courier", 18, "bold"))
my_label.grid(column=1, row=1)

#Grid and pack cant be used in the same program


my_button1 = Button(text = "Button1")
my_button2 = Button(text="Button2")
my_button1.grid(column=2, row=2)
my_button2.grid(column=3, row=1)

#Entry
entry = Entry(width=10)
#add some text to begin with
entry.insert(END, string = "Some text")
# Gets text in entry
entry.grid(column=4, row=4)


window.mainloop()