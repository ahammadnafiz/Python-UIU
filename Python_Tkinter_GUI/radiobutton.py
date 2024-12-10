from tkinter import *

# Radio Button = similar to checkbox, but you can only select one from a group

items = ['Laptop', 'Iphone', 'Water']

def display_item():
    if x.get() == 0:
        display.delete(0, END)
        display.insert(0, f"You orderd {items[0]}")
    elif x.get() == 1:
        display.delete(0, END)
        display.insert(0, f"You orderd {items[1]}")
    elif x.get() == 2:
        display.delete(0, END)
        display.insert(0, f"You orderd {items[2]}")
    else:
        display.delete(0, END)
        display.insert(0, 'HUH?')

window = Tk()
window.geometry('500x400')

label = Label(window,
              text='Select Option!',
              font=('Arial', 15, 'bold'),
              fg='#232528',
              bg='#61E786',
              relief=RAISED,
              bd=7,
              padx=10,
              pady=5)

label.pack(padx=40, pady=20)

display = Entry(window,
                font=('Arial', 20))
display.pack()

x = IntVar(value=-1)

for item in range(len(items)):
    radio_button = Radiobutton(window,
                               text=items[item],    # Adds text to radio button
                               font=('Arial', 12),                                                             variable=x,          # Groups Radiobutton together if they share the same variable 
                               value=item,           # Assigns each Radiobutton a different value                
                               padx=1000,
                               command=display_item
                               )
    radio_button.pack(anchor=W)

window.mainloop()

# some option in Radiobutton
'''
indicatoron = 0 -> Eliminate circle indicators
width = something -> Sets width of radio buttons
'''
