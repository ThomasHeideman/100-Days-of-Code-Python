from tkinter import *
from tkinter import messagebox
import json
from random import choice, randint, shuffle
from pyperclip import copy

# ---------------------------- CONSTANTS ------------------------------- #
FAVICON = "./src/favicon/favicon.ico"
FONT = "Segoe UI"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(3, 6))]
    password_numbers = [choice(numbers) for _ in range(randint(3, 6))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_input():
    url = website_entry.get().lower()
    user = email_entry.get()
    password = password_entry.get()

    new_data = {
        url: {
            "user": user,
            "password": password,
        }
    }

    missing_fields = []
    if not url:
        missing_fields.append("Website")
    if not user:
        missing_fields.append("Email or Username")
    if not password:
        missing_fields.append("Password")

    if missing_fields:
        message = "\n- ".join(missing_fields)
        messagebox.showwarning(title="Oops", message=f"You forgot the following field(s): \n- {message}")

    elif messagebox.askokcancel(title="Save Password?", message=f"These are the details entered: \nWebsite: "
                                                                f"{url} \nEmail: {user} \nPassword: {password} "
                                                                f"\nDo you want to save this password?"):

        try:
            with open("./data/data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            data = new_data
        else:
            data.update(new_data)
        finally:
            with open("./data/data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        copy(password)
        messagebox.showinfo(title="Password Saved", message=f"Password saved & copied to clipboard!")
        website_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry.delete(0, END)
        email_entry.insert(0, "email@example.com")


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    url = website_entry.get().lower()
    with open("./data/data.json", "r") as data_file:
        data = json.load(data_file)
        try:
            data[url]
        except KeyError:
            messagebox.showerror(title="Not Found", message=f"No records found for {url}")
        else:
            messagebox.showinfo(title=f"Password for {url}",
                                message=f"Email/User ID: {data[url]["user"]}\nPassword: {data[url]["password"]}\n Your password has been copied to the clipboard")
            copy(data[url]["password"])



# ---------------------------- UI SETUP ------------------------------- #
# region Window:
window = Tk()
window.title("Password Manager")
window.iconbitmap(FAVICON)
window.config(padx=30, pady=10)
canvas = Canvas(width=200, height=200)
canvas.grid(row=0, column=0, columnspan=3, padx=30, pady=(10, 0))
logo_image = PhotoImage(file="./src/logo.png")
canvas.create_image(100, 100, image=logo_image)
# endregion

# region Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="w", padx=4, pady=(0, 8))
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="w", padx=4, pady=8)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="w", padx=4, pady=8)
# endregion

# region Entries
website_entry = Entry()
website_entry.config(relief="flat",
                     highlightthickness=1,
                     highlightcolor="#3498db",
                     highlightbackground="#fff")
website_entry.grid(row=1, column=1, sticky="ew", padx=4, pady=(0, 8), ipadx=8, ipady=6)
website_entry.focus()
email_entry = Entry()
email_entry.config(relief="flat",
                   highlightthickness=1,
                   highlightcolor="#3498db",
                   highlightbackground="#fff")
email_entry.grid(row=2, column=1, columnspan=2, sticky="ew", padx=4, pady=8, ipadx=8, ipady=6)
email_entry.insert(0, "email@example.com")
password_entry = Entry()
password_entry.config(relief="flat",
                      highlightthickness=1,
                      highlightcolor="#3498db",
                      highlightbackground="#fff")
password_entry.grid(row=3, column=1, sticky="ew", padx=4, pady=8, ipadx=8, ipady=6)
# endregion

# region Buttons
search_button = Button(text="Search Password ", command=search)
search_button.config(bg="#333",
                     fg="#fff",
                     activeforeground="#fff",
                     activebackground="#3b3a3a",
                     relief="flat",
                     overrelief="flat",
                     cursor="hand2")
search_button.grid(row=1, column=2, padx=(12, 4), pady=8, ipadx=12, ipady=4)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.config(bg="#333",
                                fg="#fff",
                                activeforeground="#fff",
                                activebackground="#3b3a3a",
                                relief="flat",
                                overrelief="flat",
                                cursor="hand2")
generate_password_button.grid(row=3, column=2, padx=(12, 4), pady=8, ipadx=12, ipady=4)

add_button = Button(text="Add", width=36, command=save_input)
add_button.config(bg="#333",
                  fg="#fff",
                  activeforeground="#fff",
                  activebackground="#3b3a3a",
                  relief="flat",
                  overrelief="flat",
                  cursor="hand2")
add_button.grid(row=4, column=1, columnspan=2, sticky="ew", padx=4, pady=(8, 20), ipadx=4, ipady=4)
# endregion

window.mainloop()
