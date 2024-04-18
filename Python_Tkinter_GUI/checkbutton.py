from tkinter import *


def display_robot():
    if x.get() == 1:
        entry.delete(0, END)
        entry.insert(0, 'You are a Human')
    else:
        entry.delete(0, END)

def display_human():
    if y.get() == 1:
        entry.delete(0, END)
        entry.insert(0, 'You Feel Lonley')
    else:
        entry.delete(0, END)


window = Tk()
window.geometry('450x400')

label = Label(window,
              text='Your Opinion!',
              font=('Arial', 15, 'bold'),
              fg='#232528',
              bg='#61E786',
              relief=RAISED,
              bd=7,
              padx=10,
              pady=5)

label.pack(padx=40, pady=20)

entry = Entry(window,
              font=('Arial', 20))

entry.pack()

x = IntVar()
y = IntVar()

check_button_accept = Checkbutton(window,
                            text='Robot',
                            font=('Arial', 10, 'bold'),
                            variable=x,
                            onvalue=1,
                            offvalue=0,
                            command=display_robot,
                            padx=10,
                            pady=5)

check_button_not = Checkbutton(window,
                            text="Not Robot",
                            font=('Arial', 10, 'bold'),
                            variable=y,
                            onvalue=1,
                            offvalu=0,
                            command=display_human,
                            padx=10,
                            pady=5)

check_button_accept.pack(pady=20)
check_button_not.pack()


window.mainloop()

# Some more Uses
# BooleanVar() is used to hold a boolean (True/False) value.
# It's commonly used with Checkbutton and Radiobutton to manage binary states.
# Methods include get() and set(value) to retrieve and update the boolean value, respectively.

# StringVar() is used to hold a string value.
# It's commonly used with Entry, Label, Button, OptionMenu, etc., to manage text-based data.
# Methods include get() and set(value) to retrieve and update the string value, respectively.

