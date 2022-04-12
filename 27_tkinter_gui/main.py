import tkinter


def add(*args):
    sum = 0
    for x in args:
        sum += x
    print(sum)

def button_clicked():
    # print("clicked")
    new_t = tkinput.get()
    my_label.config(text=new_t)



window = tkinter.Tk()
window.title("My GUI")
window.minsize(width=500, height=300)


# label
my_label = tkinter.Label(text="hello", font=("Arial, 24"))
my_label.pack()

add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


button = tkinter.Button(text="CLick me", command=button_clicked)
button.pack()

tkinput = tkinter.Entry()
tkinput.pack()



window.mainloop()
