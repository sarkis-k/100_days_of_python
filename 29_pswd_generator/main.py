from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
user_ent = Entry(width=35)
user_ent.grid(column=1, row=3, columnspan=2)
passwd_ent = Entry(width=21)
passwd_ent.grid(column=1, row=4)

# buttons
passwd_gen_b = Button(text="Generate Password")#, command=)
passwd_gen_b.grid(column=2, row=4)
add_b = Button(text="Add", width=36)#, command=)
add_b.grid(column=1, row=5, columnspan=2)



window.mainloop()