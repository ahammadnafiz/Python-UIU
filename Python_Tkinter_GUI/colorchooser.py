from tkinter import *
from tkinter import colorchooser # This is a sub module

def color():
    colour = colorchooser.askcolor()
    display.delete(0, END)
    display.insert(0, str(colour[1]))
    color_hex = colour[1]
    window.config(bg=color_hex)    # Change background color

window = Tk()
window.geometry('500x400')

label = Label(window,
              text='Color Chooser',
              font=('Arial', 15, 'bold'),
              relief=GROOVE,
              borderwidth=4,
              bd=5,
              padx=10,
              pady=5,
              fg='#F3FFC6',
              bg='#182825')
label.pack(pady=20)

display = Entry(window,
                font=('Comic sans', 15))
display.pack(pady=10)

button = Button(window,
                text='Ask Color!',
                font=('Arial', 12, 'bold'),
                relief=GROOVE,
                borderwidth=10,
                bd=5,
                padx=10,
                pady=5,
                bg='#0496FF',
                fg='#FFFFFF',
                command=color)
button.pack(pady=40)
window.mainloop()
