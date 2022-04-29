from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizUI(Tk):

    def __init__(self, quiz_brain: QuizBrain):
        super().__init__()
        self.score = None
        self.quiz = quiz_brain
        self.false_b = None
        self.true_b = None
        self.question_text = None
        self.canvas = None
        self.score_label = None

    def interface(self):
        self.title("quizz")
        self.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score:{self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            100,
            width=280,
            text="Some question",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true_b = Button(image=true_img, command=self.true_click)
        self.true_b.grid(row=2, column=1)

        false_img = PhotoImage(file="images/false.png")
        self.false_b = Button(image=false_img, command=self.false_click)
        self.false_b.grid(row=2, column=0)

        self.get_next_question()

        self.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"THE END\nYour Score is {self.quiz.score}/{self.quiz.question_number}")
            self.true_b.config(state="disabled")
            self.false_b.config(state="disabled")

    def true_click(self):
        self.give_feedback(self.quiz.check_answer(user_answer="True"))

    def false_click(self):
        self.give_feedback(self.quiz.check_answer(user_answer="False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.after(1000, self.get_next_question)
