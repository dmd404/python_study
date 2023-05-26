from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website = Label(text='Website:')
website.grid(row=1, column=0)
email = Label(text='Email/Username:')
email.grid(row=2, column=0)
pwd = Label(text='Password:')
pwd.grid(row=3, column=0)

# Entry
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
pwd_entry = Entry(width=21)
pwd_entry.grid(row=3, column=1)

# Button
pwd_btn = Button(text='Generate Password')
pwd_btn.grid(row=3, column=2)
add_btn = Button(text='Add', width=36)
add_btn.grid(row=4, column=1, columnspan=2)


window.mainloop()
