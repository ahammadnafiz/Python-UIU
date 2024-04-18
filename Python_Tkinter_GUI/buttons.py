from tkinter import *

# Button = You click it, then it does stuff

count = 0

def click():
    global count
    count += 1
    print(count)

window = Tk()

window.geometry('450x400')

button = Button(window,
                text='Click Me!',
                command=click,
                font=('Comic Sans', 15),
                bg='#7371FC',
                fg= '#FFFFFC',
                relief= RAISED
                )
button.pack(pady=20)

window.mainloop()
