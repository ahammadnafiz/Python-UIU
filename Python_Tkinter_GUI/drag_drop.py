from tkinter import *

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)

window = Tk()
window.geometry('500x500')

label_1 = Label(window,
              fg='#FFFFFF',
              bg='#00A8E8',
              relief=RAISED,
              bd=7,
              padx=10,
              pady=5,
              width=10,
              height=5)
label_1.place(x=0, y=0)

label_2 = Label(window,
              fg='#FFFFFF',
              bg='#FF4A1C',
              relief=RAISED,
              bd=7,
              padx=10,
              pady=5,
              width=10,
              height=5)
label_2.place(x=300, y=200)

label_1.bind('<Button-1>', drag_start)
label_1.bind('<B1-Motion>', drag_motion)

label_2.bind('<Button-1>', drag_start)
label_2.bind('<B1-Motion>', drag_motion)


window.mainloop()
