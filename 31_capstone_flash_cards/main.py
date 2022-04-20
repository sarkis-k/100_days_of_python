from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"

def random_word():
    df = pandas.read_csv("data/french_words.csv")
    data = pandas.DataFrame.to_dict(df, "records")
    
    print(data)
    # data = pandas.DataFrame.to_dict(self="data/french_words.csv" ,orient="records")

window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Learn a Language")


canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR)
label = Label(text="FRENCH")
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas.create_image(400,263, image=card_front_img)
canvas.config(highlightthickness=0)
canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="bonjour", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

random_word()


green_b_img = PhotoImage(file="images/right.png")
green_b = Button(image=green_b_img, highlightthickness=0)
green_b.grid(column=1, row=1)
red_b_img = PhotoImage(file="images/wrong.png")
red_b = Button(image=red_b_img, highlightthickness=0)
red_b.grid(column=0, row=1)
# canvas.create_image(600,462, image=green_b_img)
# canvas.create_image(200,462, image=red_b_img)

window.mainloop()