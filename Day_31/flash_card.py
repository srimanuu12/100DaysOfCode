from cgitb import text
from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn ={}

def flip_card():
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(card_title, fill="white",text="English")
    canvas.itemconfig(card_word, fill="white",text=current_card["English"])

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=front_img)
    canvas.itemconfig(card_title, text="Korean",fill="black")
    canvas.itemconfig(card_word, text=current_card["Korean"],fill="black")
    flip_timer = window.after(3000, flip_card)
    
def is_known():
    to_learn.remove(current_card)
    word = pandas.DataFrame(to_learn)
    word.to_csv("./day_31/words_to_learn.csv",index=False)
    next_card()

window = Tk()
window.title("Flash Card")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

try:
    data = pandas.read_csv("./day_31/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./day_31/data/koreanwords.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

front_img = PhotoImage(file="./day_31/images/card_front.png")
back_img = PhotoImage(file="./day_31/images/card_back.png")
canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400,263,image=front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 30, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 30, "bold"))
canvas.grid(row=0,column=0, columnspan=2)

cross_img = PhotoImage(file="./day_31/images/wrong.png")
correct_img= PhotoImage(file="./day_31/images/right.png")
unknown_button = Button(image=cross_img, command=next_card)
unknown_button.grid(row=1,column=0)
known_button = Button(image=correct_img, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()