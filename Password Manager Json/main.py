from tkinter import  *
from tkinter import messagebox
from random import *
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")
    entry_password.insert(0, password)
    pyperclip.copy(password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_note():
    note_website = entry_website.get()
    note_email = entry_email.get()
    note_password = entry_password.get()
    new_data = {
        note_website: {
            "email":note_email,
            "password":note_password
        }
    }
            
    if len(note_password) == 0 or len(note_website) == 0:
            messagebox.showerror(title="Error", message="You shouldn't left spaces empty")
    else:
        try:
            with open ("data.json", "r") as file:
                #Reading Data
                data = json.load(file)
        except FileNotFoundError:
             with open("data.json", "w") as file:
                 json.dump(new_data, file, indent=4)    
        else:
            #Updating old data with new data
            data.update(new_data)
            
            with open("data.json", "w") as file:
                #Saving Updated Data
                json.dump(data, file, indent=4)
        finally:    
            entry_website.delete(0, END)
            entry_password.delete(0, END)   
            
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = entry_website.get()
    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}.")
        else:
            messagebox.showinfo(title="Error", message=f"You dont have files with the name {website}")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100, image = logo)
canvas.grid(row=0, column=1)

label1 = Label(text="website:")
label1.grid(row=1, column=0)

label2 = Label(text="Email/Username:")
label2.grid(row=2, column=0)

label3 = Label(text="Password:")
label3.grid(row=3, column=0)


entry_website = Entry(width=25)
entry_website.grid(row=1, column=1, columnspan=1)
entry_website.focus()

entry_email = Entry(width=35)
entry_email.grid(row=2, column=1, columnspan=2)
entry_email.insert(0, "joangabrieldj@gmail.com")

entry_password = Entry(width=25)
entry_password.grid(row=3, column=1, columnspan=1)

button1 = Button(text="Generate Password", width=15, command=generate_password)
button1.grid(row=3, column=2, columnspan=2)

button2 = Button(text="Add", width=36, command=save_note)
button2.grid(row=4, column=1, columnspan=2)

button3 = Button(text="Search", width=15, command=find_password)
button3.grid(row=1, column=2, columnspan=2)

window.mainloop()
