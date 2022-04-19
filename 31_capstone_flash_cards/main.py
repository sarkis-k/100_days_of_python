from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(bg=BACKGROUND_COLOR, height=626, width=900, padx=50, pady=50)
window.title("Learn a Language")


canvas = Canvas(height=526, width=800)
canvas.grid()



window.mainloop()