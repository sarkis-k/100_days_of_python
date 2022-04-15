from tkinter import *
from tkinter import messagebox
import random
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def passwd_gen():
    # clear the field
    passwd_ent.delete(0, END)
    # pswd generator
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for sym in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for num in range(random.randint(2, 4))]
    random.shuffle(password_list)
    password = "".join(password_list)

    # inserting pswd into the field
    passwd_ent.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_entry():
    if web_ent.get() == "" or passwd_ent.get() == "":
        messagebox.showinfo(title="Wrong Entry", message="Can't be empty")
    else:
        new_data = {
            web_ent.get(): {
                "email": user_ent.get(),
                "password": passwd_ent.get()
            }
        }
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            web_ent.delete(0, END)
            passwd_ent.delete(0, END)


# ----------------------------- SEARCH -------------------------------- #
def search():
    search_ent = web_ent.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="404", message="Not Found")
    else:
        if search_ent in data:
            email = data[search_ent]["email"]
            pswd = data[search_ent]["password"]
            messagebox.showinfo(title=search_ent, message=f"email: {email}\npassword: {pswd}")
        else:
            messagebox.showinfo(title="404", message="No entry such that")


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
user_l = Label(text="Email/Username:")
user_l.grid(column=0, row=3)
passwd_l = Label(text="Password:")
passwd_l.grid(column=0, row=4)

# entries
web_ent = Entry(width=21)
web_ent.grid(column=1, row=2)
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
search_b = Button(text="Search", width=15, command=search)
search_b.grid(column=2, row=2)

window.mainloop()
