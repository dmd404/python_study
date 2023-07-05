from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"
HEIGHT = 526
WIDTH = 800

# ---- UI
window = Tk()
window.title('flash card')
window.config(padx=50, pady=50)


canvas = Canvas(window, height=HEIGHT, width=WIDTH)
card_img = PhotoImage(file='images/card_front.png')
canvas.create_image(WIDTH/2, HEIGHT/2, anchor='center', image=card_img)
canvas.grid(row=0, columnspan=2)

wrong_img = PhotoImage(file='images/wrong.png')
right_img = PhotoImage(file='images/right.png')
wrong_label = Label(window, image=wrong_img)
wrong_label.grid(row=1, column=0)
right_label = Label(window, image=right_img)
right_label.grid(row=1, column=1)

window.mainloop()
