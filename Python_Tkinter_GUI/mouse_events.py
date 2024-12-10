from tkinter import *

def doSomething(event):
    label.config(text=f"({event.x},{event.y})")

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

#window.bind('<Button-1>', doSomething)  # Left mouse click
#window.bind('<Button-3>', doSomething)  # Right mouse click
#window.bind('<ButtonRelease>', doSomething)
#window.bind('<Enter>', doSomething)
#window.bind('<Leave>', doSomething)
window.bind('<Motion>', doSomething)

label = Label(window,
              font=('Arial', 25, 'bold'),
              fg='black',
              padx=10,
              pady=5)
label.pack(pady=20)

window.mainloop()
