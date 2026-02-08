from tkinter import *
import pandas
import random
import pandas as pd

BACKGROUND_COLOR = "#1E2933"
FONT = "Segoe UI"
flip_timer = None
current_card = {}

try:
    data = pd.read_csv("./data/terms_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("./data/python_terms.csv")

words_to_learn = data.to_dict(orient="records")

def next_card():
    global flip_timer, current_card
    if flip_timer :
        window.after_cancel(flip_timer)
    canvas.itemconfig(card_img, image=front_img)
    current_card = random.choice(words_to_learn)
    title = list(current_card.keys())[0]
    canvas.itemconfig(card_title, text=title,fill="#1e2933")
    canvas.itemconfig(card_word, text=current_card["Python Term"],font=(FONT,50, "bold"),fill="#1e2933")
    flip_timer = window.after(3000, flip_card)

def flip_card():
    global current_card
    canvas.itemconfig(card_img, image=back_img)
    title = list(current_card.keys())[1]
    canvas.itemconfig(card_title, text=title,fill="#FFF")
    canvas.itemconfig(card_word, text=current_card["Meaning"], font=(FONT,20, "italic"),fill="#FFF")


def is_correct():
    global current_card
    words_to_learn.remove(current_card)
    df = pd.DataFrame(words_to_learn)
    df.to_csv("./data/terms_to_learn.csv", index=False)
    next_card()


#  region ---------------------------- UI ----------------------------------------------- #

window = Tk()
window.title("Python Flash Cards")
window.iconbitmap("./images/Learn_Python.ico")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
card_img = canvas.create_image(400,263, image=front_img)
canvas.grid(row=0, column=0, columnspan=2,pady=(0,10))
card_title= canvas.create_text(400,160, text="",font=(FONT, 40, "italic"),fill="#1e2933")
card_word = canvas.create_text(400,273, text="",font=(FONT, 50, "bold"),fill="#1e2933")


btn_wrong_img = PhotoImage(file="./images/wrong.png")
btn_right_img = PhotoImage(file="./images/right.png")

button_wrong = Button(image=btn_wrong_img, command=next_card)
button_wrong.config(  highlightthickness=0,
                      borderwidth=0,
                      activebackground=BACKGROUND_COLOR,
                      relief="flat",
                      overrelief="flat",
                      cursor="hand2")

button_wrong.grid(row=1, column=0)

button_right = Button(image=btn_right_img, command=is_correct)
button_right.config( highlightthickness=0,
                     borderwidth=0,
                     activebackground=BACKGROUND_COLOR,
                     relief="flat",
                     overrelief="flat",
                     cursor="hand2")
button_right.grid(row=1, column=1)
# endregion

next_card()


mainloop()
