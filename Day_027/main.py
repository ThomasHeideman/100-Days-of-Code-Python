from tkinter import *

def button_click():
    # my_label.config(text="Button Got Clicked")
    my_label.config(text=my_input_field.get())
def new_button_click():
    window.config(background="yellow")
    my_label.config(background="yellow")

# region Window
window = Tk()
window.title("My first GUI")
window.minsize(width=800, height=600)
window.config(padx=32,pady=32)

# endregion

# region Label
my_label = Label(text="My first GUI Label", font=("Arial", 24, "bold"))
my_label.config(padx=16,pady=16)
# my_label.config(text="Another new text")
# my_label["text"] = "New text"
# my_label.pack()
# my_label.place(x=100,y=200)
my_label.grid(column=0,row=0)
# endregion

# region Button
my_button = Button(text="My First Button", font=("Arial", 14, "normal"), command=button_click)
my_button.config(fg="white", activeforeground="white", width=16, padx=8,pady=4)
my_button["background"] = "red"
my_button["activebackground"] = "dark red"

my_new_button = Button(text="My Second Button", font=("Arial", 14, "normal"), command=new_button_click)
my_new_button.config( fg="white", activeforeground="white", width=16, padx=8,pady=4)
my_new_button["background"] = "green"
my_new_button["activebackground"] = "dark green"

my_button.grid(row=1,column=1, padx=16,pady=8)
my_new_button.grid(row=0,column=2, padx=16,pady=8)
# my_button.pack(pady=16)
# endregion

# region Entry
my_input_field = Entry(width=32,font=("Arial", 14, "normal"))
my_input_field.insert(END, string="Type something...")

# input_field.pack(pady=16, ipadx=4, ipady=4 )
my_input_field.grid(row=2,column=3,  padx=16,pady=8, ipady=4, ipadx=4)
# endregion

window.mainloop()