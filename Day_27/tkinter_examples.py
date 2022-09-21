from tkinter import *

window = Tk()
window.title("First GUI program")
window.minsize(width= 500, height= 600)

# Label
my_label = Label(text = "Old Text", font = ("Courier", 18, "bold"))
my_label.pack() # Initialize label It packs label onto the screen and display Label text

#Grid and pack cant be used in the same program
#my_label.grid(column = 1, row = 3)
# BUtton
def action():
    my_label.config(text=entry.get())

my_button = Button(text = "Click me", command=action)
my_button.pack()

#Entry
entry = Entry(width=30)
#add some text to begin with
entry.insert(END, string = "Some text")
# Gets text in entry
entry.pack()

#Text
text = Text(height=5, width = 20)
#Put cursor in the textbox
text.focus()
# Add some text to begin with
text.insert(END, "Example of multi-line text")
#Gets current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

# Spinbox
def spinbox_used():
    #gets current value in spinbox
    print(spinbox.get())
spinbox = Spinbox(from_= 0,to=10, width = 5, command=spinbox_used)
spinbox.pack()

#Scale
def scale_used(value):
    #Gets current value in Scaler
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbox
def checkbutton_used():
    #prints 1 button checked, if not 0
    print(checked_state.get())
checked_state = IntVar()
checkbutton = Checkbutton(text="IS_ON?", variable = checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox

def listbox_used():
    #gets current selection from listbox
    print(listbox.get(listbox.curselection()))
listbox = Listbox(height=3)
cars = ["MG", "T","H"]
for item in cars:
    listbox.insert(cars.index(item), item)
listbox.bind("<<ListboxSelect>>",listbox_used)
listbox.place(x=100, y=200) 

window.mainloop()