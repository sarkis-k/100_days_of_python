from tkinter import *
from tkinter import messagebox
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def passwd_gen():
    passwd_ent.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for sym in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for num in range(random.randint(2, 4))]
    random.shuffle(password_list)
    password = "".join(password_list)

    passwd_ent.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_entry():
    if web_ent.get() == "" or passwd_ent.get() == "":
        messagebox.showinfo(title="Wrong Entry", message="Can't be empty")
    else:
        is_ok = messagebox.askokcancel(title=web_ent.get(), message=f"These are the details entered: \n"
                                                                    f"Email: {user_ent.get()}\n"
                                                                    f"Password: {passwd_ent.get()}\n"
                                                                    f"Is it ok to save?")
        if is_ok:
            with open(file="data.txt", mode="a") as file:
                file.write(f"{web_ent.get()} | {user_ent.get()} | {passwd_ent.get()} \n")
            web_ent.delete(0, END)
            passwd_ent.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=1)

# labels
web_l = Label(text="Website:")
web_l.grid(column=0, row=2)
user_l = Label(text="Email/Usermane:")
user_l.grid(column=0, row=3)
passwd_l = Label(text="Password:")
passwd_l.grid(column=0, row=4)

# entries
web_ent = Entry(width=35)
web_ent.grid(column=1, row=2, columnspan=2)
web_ent.focus()
user_ent = Entry(width=35)
user_ent.grid(column=1, row=3, columnspan=2)
user_ent.insert(0, "smith@mail.com")
passwd_ent = Entry(width=21)
passwd_ent.grid(column=1, row=4)

# buttons
passwd_gen_b = Button(text="Generate Password", command=passwd_gen)
passwd_gen_b.grid(column=2, row=4)
add_b = Button(text="Add", width=36, command=add_entry)
add_b.grid(column=1, row=5, columnspan=2)

window.mainloop()
