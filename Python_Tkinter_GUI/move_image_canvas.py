from tkinter import *

def move_up(event):
    canvas.move(my_ufo, 0, -10)

def move_down(event):
    canvas.move(my_ufo, 0, 10)

def move_left(event):
    canvas.move(my_ufo, -10, 0)

def move_right(event):
    canvas.move(my_ufo, 10, 0)


window = Tk()
window.geometry('600x600')

label = Label(window,
              text='Canvas',
              font=('Arial', 15, 'bold'),
              fg='#FFFFFF',
              bg='#00A8E8',
              relief=RAISED,
              bd=7,
              padx=10,
              pady=5)
label.pack(pady=20)

canvas = Canvas(window,
                width=500,
                height=500)
canvas.pack()

ufo = PhotoImage(file = 'ufo.png')
my_ufo = canvas.create_image(0, 0, image=ufo, anchor=NW)


window.bind('<w>', move_up) 
window.bind('<s>', move_down) 
window.bind('<a>', move_left) 
window.bind('<d>', move_right)

window.bind('<Up>', move_up) 
window.bind('<Down>', move_down) 
window.bind('<Left>', move_left) 
window.bind('<Right>', move_right)

window.mainloop()
