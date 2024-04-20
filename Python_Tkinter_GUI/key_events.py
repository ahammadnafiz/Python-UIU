from tkinter import *

def function(event):
    label.config(text=event.keysym)


window = Tk()
window.geometry('500x300')

label = Label(window,
              text='Event!',
              font=('Arial', 15, 'bold'),
              fg='#FFFFFF',
              bg='#00A8E8',
              relief=RAISED,
              bd=7,
              padx=10,
              pady=5)
label.pack(pady=20)

window.bind('<Key>', function)

label = Label(window,
              font=('Arial', 25, 'bold'),
              fg='black',
              padx=10,
              pady=5)
label.pack(pady=20)


window.mainloop()
