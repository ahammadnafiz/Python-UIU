from tkinter import *

# Canvas = widget that is used to draw graps, plots, images in window

window = Tk()

canvas = Canvas(window,
                height=500,
                width=500)
canvas.pack()

# Draw Shapes
canvas.create_rectangle(50, 50, 200, 150, fill="blue")
canvas.create_oval(250, 50, 350, 150, fill="red")
canvas.create_line(50, 200, 200, 250, fill="green")
canvas.create_polygon(300, 200, 350, 250, 250, 250, fill="yellow",
                      outline='black')
#canvas.create_arc(0,0, 500,500)

# Add Text
canvas.create_text(200, 200, text="Hello, Canvas!", fill="black", font=("Arial", 16))

window.mainloop()
