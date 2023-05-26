from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    pwd = pwd_entry.get()
    website_entry.delete(0, 'end')
    email_entry.delete(0, 'end')
    pwd_entry.delete(0, 'end')
    with open("my_data.txt", "a") as file:
        file.write(f'{website} | {email} | {pwd} \n')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)
email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)
pwd_label = Label(text='Password:')
pwd_label.grid(row=3, column=0)

# Entry
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, '@email.com')
pwd_entry = Entry(width=21)
pwd_entry.grid(row=3, column=1)

# Button
pwd_btn = Button(text='Generate Password')
pwd_btn.grid(row=3, column=2)
add_btn = Button(text='Add', width=36, command=save)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
