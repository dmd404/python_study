from tkinter import *

window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)


def button_clicked():
    # my_label['text'] = 'I Got Clicked'
    new_text = int(input.get())
    km.config(text=new_text*1.6)


# text
# txt_miles = Label(text="Miles", font=('Arial', 24, 'bold'))
# txt_miles.config(text='test')
# txt_miles.grid(column=2, row=0)
# txt2 = Label(text="is equal to", font=('Arial', 24, 'bold'))
# txt3 = Label(text="Km", font=('Arial', 24, 'bold'))
my_txt = Label(text='Miles', font=('Arial', 24, 'bold'))
my_txt.grid(column=2, row=0)

my_txt1 = Label(text='is equal to', font=('Arial', 24, 'bold'))
my_txt2 = Label(text='Km', font=('Arial', 24, 'bold'))
km = Label(text=0)
km.grid(column=1, row=1)
my_txt1.grid(column=0, row=1)
my_txt2.grid(column=2, row=1)
# Button
button = Button(text='Calculate', command=button_clicked)
button.grid(column=1, row=2)


# Entry
input = Entry(width=10)
input.grid(column=1, row=0)

window.mainloop()