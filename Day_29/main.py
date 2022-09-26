from tkinter import messagebox
from tkinter import *
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'X', 'W', 'Y', 'Z']
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+" , "-", ".", "/", ":", ";", "<", "=", ">", "?", "@",  "[",  "]", "^",  "_", "{", "|", "}", "~"]

    no_letter = random.randint(5,6)
    no_numbers = random.randint(3,4)
    no_symbols = random.randint(2,3)

    password_letters = [random.choice(letters) for _ in range(no_letter)]
    password_symbols = [random.choice(symbols) for _ in range(no_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(no_numbers)]

    password_list = password_letters+password_numbers+password_symbols
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    username = email_entry.get()
    paswd = password_entry.get()

    if len(website) == 0 or len(paswd) == 0:
        messagebox.showerror(title="Error", message="Please don't leave any empty fields!")
    else:
        is_true = messagebox.askokcancel(title=website, message=f"Email/Username: {username}\nPassword:{paswd}\nIs to ok to save?")
        
        if is_true:
            with open("./day_29/data.txt", "a+") as file:
                file.write(f"{website} | {username} | {paswd}\n")
            website_entry.delete(0,END)
            email_entry.delete(0,END)
            email_entry.insert(0,"user@gmail.com")
            password_entry.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="./day_29/logo.png")
canvas.create_image(100,100,image = logo)
canvas.grid(row=0, column=1)

#Labels
website_label=Label(text="Website:")
website_label.grid(row=1,column=0)
email_label=Label(text="Email/Username:")
email_label.grid(row=2,column=0)
password_label=Label(text="Password:")
password_label.grid(row=3,column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1,columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"user@gmail.com")
password_entry = Entry(width=17)
password_entry.grid(row=3,column=1)

#Buttons
generate_password=Button(text="Generate Password", command=password_gen)
generate_password.grid(row=3,column=2)
add=Button(text="Add",width=35, command=save_data)
add.grid(row=4, column=1,columnspan=2)

window.mainloop()