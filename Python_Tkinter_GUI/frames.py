from tkinter import *

# Frame = a rectangular container to group and hold widgets

window = Tk()
window.geometry('600x500')

label = Label(window,
              text='Frames',
              font=('Arial', 15, 'bold'),
              fg='#FFFFFF',
              bg='#00A8E8',
              relief=RAISED,
              bd=7,
              padx=10,
              pady=5)
label.pack(pady=60)

frame = Frame(window,
              bg='#F1FAEE',
              bd=5,
              relief=GROOVE)
frame.place(x=200, y=200)
#frame.pack(side=BOTTOM)

Button(frame,
                text='W',
                font=('Arial', 12, 'bold'),
                relief=GROOVE,
                borderwidth=10,
                bd=5,
                padx=10,
                pady=5,
                bg='#006992',
                fg='#EAF8BF',).pack(side=TOP, padx=5, pady=5)
Button(frame,
                text='A',
                font=('Arial', 12, 'bold'),
                relief=GROOVE,
                borderwidth=10,
                bd=5,
                padx=10,
                pady=5,
                bg='#006992',
                fg='#EAF8BF',).pack(side=LEFT, padx=5, pady=5)
Button(frame,
                text='S',
                font=('Arial', 12, 'bold'),
                relief=GROOVE,
                borderwidth=10,
                bd=5,
                padx=10,
                pady=5,
                bg='#006992',
                fg='#EAF8BF',).pack(side=LEFT, padx=5, pady=5)
Button(frame,
                text='D',
                font=('Arial', 12, 'bold'),
                relief=GROOVE,
                borderwidth=10,
                bd=5,
                padx=10,
                pady=5,
                bg='#006992',
                fg='#EAF8BF',).pack(side=LEFT, padx=5, pady=5)


window.mainloop()
