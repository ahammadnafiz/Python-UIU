from tkinter import *
from tkinter import messagebox

# Listbox = A listing of selectable text items within it's containter

def submit_item():
    info = 'Your order is confirmed'
    messagebox.showinfo('Success', info)

def add_item():
    listbox.insert(listbox.size(), display.get())
    listbox.config(height=listbox.size())

def delete_item():
    listbox.delete(listbox.curselection())
    #for index in reversed(listbox.curselection()):     If MULTIPLE selectmode is on
        #listbox.delete(index)
    listbox.config(height=listbox.size())

window = Tk()
window.geometry('600x600')

label = Label(window,
              text='Your Cart!',
              font=('Arial', 15, 'bold'),
              fg='#232528',
              bg='#61E786',
              relief=RAISED,
              bd=7,
              padx=10,
              pady=5
              )

label.pack(padx=40, pady=20)

items = ['Laptop', 'Business Suit', 'Briefcase', 'Notebook', 'Pen Set']

listbox = Listbox(window,
                  font=('Helvetica', 12),
                   bg='#ECEBE4',)
                   # selectmode=MULTIPLE)

listbox.pack(pady=10)

for item in range(len(items)):
    listbox.insert(item, items[item])
listbox.config(height=listbox.size())


display = Entry(window,
                font=('Arial', 20)
                )
display.pack(pady=10)

submit = Button(window,
                font=('Arial', 12),
                bg='#272838',
                text='Submit',
                fg='#FEF9FF',
                relief=RAISED,
                bd=5,
                padx=10,
                pady=5,
                command=submit_item)
submit.pack(pady=10)

add = Button(window,
                font=('Arial', 12),
                bg='#272838',
                text='Add Item',
                fg='#FEF9FF',
                relief=RAISED,
                bd=5,
                padx=10,
                pady=5,
                command=add_item)
add.pack(pady=5)

delete = Button(window,
                font=('Arial', 12),
                bg='#272838',
                text='Delete Item',
                fg='#FEF9FF',
                relief=RAISED,
                bd=5,
                padx=10,
                pady=5,
                command=delete_item)
delete.pack(pady=5)

window.mainloop()
