from tkinter import *

# Entry widget = textbox that accepts a single line of user input

def submit():
    user = entry.get()
    print(user)

def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get()) - 1, END)

window = Tk()
window.geometry('480x200')

entry = Entry(window,
              font=('Arial', 15),
              bg='#0A090C',
              fg='#16DB65')
              #show='*')

entry.pack(padx=50, pady=20)

submit_button = Button(window, text='Submit', command=submit)
submit_button.pack(padx=70, pady=5)

delete_button = Button(window, text='Delete', command=delete)
delete_button.pack(padx=70, pady= 5)

backspace_button = Button(window, text='Backspace', command=backspace)
backspace_button.pack(padx=70, pady=5)

window.mainloop()

# Some Userfull methods

'''
entry.insert(index, string)
entry.config(**options)
-> Options like: state, bg, show
'''
