from tkinter import *


def show():
    display.delete(0, END)
    display.insert(0, str(scale.get()))

window = Tk()
window.geometry('500x400')

label = Label(window,
              text='Select Size!',
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
display.pack(pady=10)

scale = Scale(window,
              from_=0,
              to=100,
              orient=HORIZONTAL,    # Orientation of scale
			  length=300,  # Length of the scale
              showvalue=1,  # Show the selected value on the scale,  If 0 hide current value
              tickinterval=20,  # Interval between ticks
              resolution=1,  # Resolution of the scale
              sliderlength=20,  # Length of the slider
              sliderrelief=RAISED,  # Relief style of the slider
              bg="lightgray",  # Background color
              fg="blue" ) # Foreground color

# scale.set() Sets current value of slider

scale.pack(pady=20)

button = Button(window,
                text='Submit',
                font=('Arial', 12),
                bg='#272838',
                fg='#FEF9FF',
                relief=RAISED,
                bd=5,
                padx=10,
                pady=5,
                command=show)
button.pack(pady=20)

window.mainloop()
