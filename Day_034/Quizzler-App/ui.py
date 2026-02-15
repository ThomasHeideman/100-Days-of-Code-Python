from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain ):
        self.quiz = quiz_brain
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.true_img = PhotoImage(file="./images/true.png")
        self.false_img = PhotoImage(file="./images/false.png")

        self.score_text=Label(text=f"score: {self.score}", bg=THEME_COLOR, font=("Arial", 12, "normal"),fg="#FFF")
        self.score_text.grid(row=0,column=1, sticky="e")

        self.canvas = Canvas(width=300,height=250, highlightthickness=0)
        self.question = self.canvas.create_text(150,125,text="")
        self.canvas.itemconfig(self.question, fill=THEME_COLOR,font=("Arial", 20, "italic"),width=260)
        self.canvas.grid(row=1,column=0,columnspan=2, pady=50)



        self.button_true=Button(image=self.true_img, command=self.true_pressed)
        self.button_true.config(highlightthickness=0,
                                borderwidth=0,
                                relief="flat",
                                overrelief="flat",
                                cursor="hand2")
        self.button_true.grid(row=2,column=0)

        self.button_false = Button(image=self.false_img, command=self.false_pressed)
        self.button_false.config(highlightthickness=0,
                                 borderwidth=0,
                                 relief="flat",
                                 overrelief="flat",
                                 cursor="hand2")
        self.button_false.grid(row=2, column=1)

        self.get_next_question()



        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question, fill=THEME_COLOR)
        if self.quiz.still_has_questions():
            self.score_text.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question,text=q_text)
        else:
            self.canvas.itemconfig(self.question,text="You've reached the end of the quiz.")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")


    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.feedback(is_right)

    def feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.question,fill="#FFF")
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.question, fill="#FFF")
        self.window.after(1000, self.get_next_question)

