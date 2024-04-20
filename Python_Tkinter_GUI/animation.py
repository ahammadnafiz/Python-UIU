from tkinter import *
import time


WIDTH = 500
HEIGHT = 500

x_velocity = 0.5
y_velocity = 1

window = Tk()
window.geometry('500x500')


canvas = Canvas(window,
                width=WIDTH,
                height=HEIGHT)
canvas.pack()

ufo = PhotoImage(file = 'ufo.png')
my_image = canvas.create_image(0, 0, image=ufo, anchor=NW)

image_height = ufo.height()
image_width = ufo.width()

while True:
    coordinates = canvas.coords(my_image)
    print(coordinates)
    
    if (coordinates[0] >= (WIDTH - image_width) or coordinates[0] < 0):
        x_velocity = -x_velocity

    if (coordinates[1] >= (HEIGHT - image_height) or coordinates[1] < 0):
        y_velocity = -y_velocity

    canvas.move(my_image, x_velocity, y_velocity)
    window.update()
    time.sleep(0.001)

window.mainloop()

