from tkinter import *

window = Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)


def button_clicked():
    # my_label['text'] = 'I Got Clicked'
    new_text = input.get()
    my_label.config(text=new_text)


# Label
my_label = Label(text="I'm a label", font=('Arial', 24, 'bold'))
my_label.config(text='new text')
my_label.grid(column=0, row=0)

# Button
button = Button(text='click me', command=button_clicked)
button.grid(column=1, row=1)
new_button = Button(text='new button')
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
input.grid(column=3, row=2)

window.mainloop()