from tkinter import *

# Label = An area widget that holds text and/or an image whithin a window

window = Tk()

window.geometry('450x450')

# Create a label widget
label = Label(window, 
              text="Hello, Tkinter!", 
              font=('Helvetica', 18, 'bold'), 
              bg='#0A2239', 
              fg='#F5E2C8', 
              justify='center', 
              borderwidth=4, 
              relief= RAISED,
              bd=10,
              padx=10, 
              pady=5)

# Pack the label widget into the main window
label.pack()


#label.place(x=50, y=50)


window.mainloop()
