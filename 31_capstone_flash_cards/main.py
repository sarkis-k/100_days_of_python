from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"

try:
    df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("data/french_words.csv")

data = pandas.DataFrame.to_dict(df, "records")
word_couple = {}


def random_word():
    global word_couple, flip_timer
    word_couple = random.choice(data)
    window.after_cancel(flip_timer)
    canvas.itemconfigure(bg_img, image=card_front_img)
    canvas.itemconfigure(fr_word_id, text=word_couple["French"], fill="black")
    canvas.itemconfigure(lg_word_id, text="French", fill="black")
    flip_timer = window.after(3000, func=flip_side)


def flip_side():
    canvas.itemconfigure(bg_img, image=card_back_img)
    canvas.itemconfigure(fr_word_id, text=word_couple["English"], fill="white")
    canvas.itemconfigure(lg_word_id, text="English", fill="white")


def known_func():
    data.remove(word_couple)
    print(len(data))

    new_data_to_learn = pandas.DataFrame(data)
    new_data_to_learn.to_csv("data/words_to_learn.csv", index=False)
    random_word()


window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Learn a Language")

flip_timer = window.after(3000, func=flip_side)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR)
label = Label(text="FRENCH")
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
bg_img = canvas.create_image(400, 263, image=card_front_img)
canvas.config(highlightthickness=0)
lg_word_id = canvas.create_text(400, 150, text="Language", font=("Ariel", 40, "italic"))
fr_word_id = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

random_word()

green_b_img = PhotoImage(file="images/right.png")
green_b = Button(image=green_b_img, highlightthickness=0, command=known_func)
green_b.grid(column=1, row=1)
red_b_img = PhotoImage(file="images/wrong.png")
red_b = Button(image=red_b_img, highlightthickness=0, command=random_word)
red_b.grid(column=0, row=1)

window.mainloop()
