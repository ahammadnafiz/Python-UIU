from tkinter import *

def create_window():
    #new_window = Toplevel() # Toplevel() = New window 'on top' of other window, linked to a 'bottom' window
    new_window = Tk()   # New independent window

window = Tk()
window.geometry('500x450')

display = Label(window,
                text='New Window Creation',
                font=('Arial', 20),
                relief=RAISED,
                bd=5,
                fg='#FDF5BF',
                bg='#252323',
                padx=10,
                pady=5)
display.pack(pady=20)

Button(window, 
       text='New Window', 
       font=('Helveitca', 15),
       relief=GROOVE,
       bd=5,
       bg='#009FB7',
       fg='#F4F4F8',
       borderwidth=3,
       padx=5,
       pady=3,
       command=create_window).pack(pady=40)

window.mainloop()
