from ctypes import windll
from tkinter import *
import math

try:
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass
# region --------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
LIGHT_YELLOW ="#FCFBF1"
YELLOW = "#f7f5dd"
DARK_YELLOW= "#deddc7"
DARK_GREY = "#31312c"
PRIMARY_FONT_NAME = "Courier"
SECONDARY_FONT_NAME = "Segoe UI"
WORK_MIN = .25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
favicon = "./src/favicon/favicon.ico"

reps = 0
timer = 0
# endregion

# region --------------------- FUNCTIONS ------------------------------- #


# ---------------------------- TIMER RESET ----------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="25:00")
    title.config(text="Timer", fg=GREEN)
    pommodoro_count.config(text="")
    reps = 0


# ------------------------- TIMER MECHANISM ---------------------------- #

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title.config(text="Break Time", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title.config(text="Break Time", fg=PINK)
    else:
        count_down(work_sec)
        title.config(text="Let's Work", fg=GREEN)

    work_sessions = math.floor(reps / 2)
    marks = "✔" * work_sessions
    pommodoro_count.config(text=marks)

    # update_tomato_icons()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_minute = math.floor(count / 60)
    count_second = count % 60
    if count_minute < 10:
        count_minute = f"0{math.floor(count_minute)}"
    if count_second < 10:
        count_second = f"0{math.floor(count_second)}"

    canvas.itemconfig(timer_text,text=f"{count_minute}:{count_second}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down, count - 1)
    else:
        start_timer()
        window.attributes("-topmost", 1)
        window.attributes("-topmost", 0)

# WARNING: Design Rabbithole ahead! 🐰
# Commented out to prevent over-polishing before the app actually works.
# Revisit image-based icons later.
# # ---------------------------- TOMATO COUNT ------------------------------- #
#
#
# def update_tomato_icons():
#     for widget in pommodoro_count.winfo_children():
#         widget.destroy()
#
#     work_sessions = math.floor(reps / 2)
#
#     for _ in range(work_sessions):
#         icon_label = Label(pommodoro_count, image=tiny_tomato_img, bg=YELLOW)
#         icon_label.pack(side="left", padx=2)


# endregion ---------------------------------------------------------------------- #


# region ---------------------- UI SETUP ------------------------------- #
#  region Window
window = Tk()
window.title("Pomodoro Timer")
window.minsize(width=600, height=600)
window.config(padx=160, pady=96,background=YELLOW)
window.iconbitmap(favicon)
# endregion

#  region Canvas
canvas = Canvas(width=480, height=536,background=YELLOW, highlightthickness=0)
tiny_tomato_img = PhotoImage(file="./src/favicon/favicon-32x32.png")
tomato_img = PhotoImage(file="./src/tomato-lg.png")
canvas.create_image(240,268, image=tomato_img)
timer_text = canvas.create_text(242,308, text="25:00", font=(PRIMARY_FONT_NAME,24,"bold"), fill="#FFF")
canvas.grid(row=1,column=1)
# endregion

#  region Title
title = Label(text="Timer", font=(PRIMARY_FONT_NAME, 32, "bold"), width=10)
title.config(background=YELLOW, fg=GREEN)
title.grid(row=0, column=1, pady=48)
# endregion

#  region checkmarks
pommodoro_count = Label(text="", font=(PRIMARY_FONT_NAME, 16, "bold"), width=8)
pommodoro_count.config( background=YELLOW, fg=GREEN)
pommodoro_count.grid(row=2, column=1,sticky="ew")
# endregion


# region Buttons
button_start = Button(text="Start", font=("Segoe UI", 12, "bold"), command=start_timer)
button_start.config(fg=DARK_GREY,
                    bg=LIGHT_YELLOW,
                    activeforeground=DARK_GREY,
                    activebackground=DARK_YELLOW,
                    width=12,
                    pady=6,
                    relief="flat",
                    overrelief="flat",
                    cursor="hand2",
                    highlightthickness=0,
                    bd=0)
button_start.grid(row=2, column=0, pady=32, sticky="e")


button_reset = Button(text="Reset", font=("Segoe UI", 12, "bold"), command=reset_timer)
button_reset.config(fg=DARK_GREY,
                    bg=LIGHT_YELLOW, 
                    activeforeground=DARK_GREY,
                    activebackground=DARK_YELLOW,
                    width=12,
                    pady=6,
                    relief="flat",
                    overrelief="flat",
                    cursor="hand2",
                    highlightthickness=0,
                    bd=0)
button_reset.grid(row=2, column=3, pady=32, sticky="w")

# endregion
# endregion

window.mainloop()