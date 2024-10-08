# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# Password Generator Project
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password = []

    password_letters = [choice(letters) for let in range(randint(8, 10))]
    password_symbol = [choice(symbols) for sym in range(randint(2, 4))]
    password_numbers = [choice(numbers) for num in range(randint(2, 4))]

    password_list = password_numbers + password_letters + password_symbol
    shuffle(password)
    password = "".join(password_list)
    pass_entry.insert(0,password)
    pyperclip.copy(password)




# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    # messagebox.showinfo(title="Title",message="Message") # a new pop up message box

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",message="Please don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                          f"\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            with open("data.txt","a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                web_entry.delete(0, END)
                pass_entry.delete(0, END)
                messagebox.showinfo(title="Successful",message="Password saved successfully" )
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

website_label = Label(text="Website")
website_label.grid(row=1,column=0)

email_label = Label(text = "Email/Username")
email_label.grid(row=2,column=0)

pass_label = Label(text="Password")
pass_label.grid(row=3,column=0)

#Entry
web_entry = Entry(width=42)
web_entry.grid(row=1,column=1, columnspan=2)
web_entry.focus()
email_entry = Entry(width=42)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0, "me@gmail.com")
pass_entry = Entry(width=24)
pass_entry.grid(row=3,column=1)

# Buttons
pass_button = Button(text="Generate Password",width=14,command=generate_pass)
pass_button.grid(row=3,column=2)

add_button = Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)



window.mainloop()

