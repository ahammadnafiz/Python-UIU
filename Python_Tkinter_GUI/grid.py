from tkinter import *

# grid() = geometry manager that organizes widget in a table like structure

window = Tk()
window.geometry('500x450')

label = Label(window,
              text='File!',
              font=('Arial', 10, 'bold'),
              fg='#FFFFFF',
              bg='#00A8E8',
              relief=RAISED,
              bd=7,
              padx=10,
              pady=5)
label.grid(row=0, column=0, columnspan=2)

firstNameLabel = Label(window, text='First Name: ', font=('Arial', 12), fg='#131515').grid(row=1, column=0)
firstNameEntry = Entry(window, font=('Arial', 12)).grid(row=1, column=1)

lastNameLabel = Label(window, text='Last Name: ', font=('Arial', 12), fg='#131515').grid(row=2, column=0)
lastNameEntry = Entry(window, font=('Arial', 12)).grid(row=2, column=1)

emailLabel = Label(window, text='Email: ', font=('Arial', 12), fg='#131515').grid(row=3, column=0)
emailentry = Entry(window, font=('Arial', 12)).grid(row=3, column=1)

Button(window,
                text='Save',
                font=('Arial', 10, 'bold'),
                relief=GROOVE,
                borderwidth=10,
                bd=5,
                padx=10,
                pady=5,
                bg='#006992',
                fg='#EAF8BF',).grid(row=4, column=0, columnspan=2)

window.mainloop()
