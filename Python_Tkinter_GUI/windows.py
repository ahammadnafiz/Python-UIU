from tkinter import *


# Widgets = GUI elements: buttons, textboxes, lables, images
# Windows = Serve as a container to hold or contain these Widgets

window = Tk() # Instantiate an instance of a window
window.geometry("420x420")
window.title('Window GUI Programe')

icon = PhotoImage(file = 'icon.png')
window.iconphoto(True, icon)

window.config(background='black')


window.mainloop()   # Place window on computer screen, listen for events
