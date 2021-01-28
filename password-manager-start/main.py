from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

def generate_password():
    password_list = []

    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    new_email = entry_email_username.get()
    new_password = entry_password.get()
    new_website = entry_website.get()

    if len(new_website) == 0 or len(new_password) == 0:
        messagebox.showinfo(title="warning!", message="One or more required fields are empty!")
        return

    is_ok = messagebox.askokcancel(title=new_website, message=f"These are the details entered:\nEmail: {new_email}\nPassword: {new_password}\n Is it ok?")
    if is_ok:
        with open("data.txt", "a") as data:
            data.write(f"{new_website} | {new_email} | {new_password}\n")
        entry_website.delete(0, END)
        entry_password.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

entry_website = Entry(width=52)
entry_website.grid(column=1, row=1, columnspan=2)
entry_website.focus()

label_email_username = Label(text="Email/Username:")
label_email_username.grid(column=0, row=2)

entry_email_username = Entry(width=52)
entry_email_username.grid(column=1, row=2, columnspan=2)
entry_email_username.insert(0, "h264matsumoto@gmail.com")

label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

entry_password = Entry(width=33)
entry_password.grid(column=1, row=3)

button_generate_pass = Button(text='Generate Password', command=generate_password)
button_generate_pass.grid(column=2, row=3)

button_add = Button(text='Add', width=44, command=save)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()