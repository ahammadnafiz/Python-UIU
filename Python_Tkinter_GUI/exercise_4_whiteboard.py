from tkinter import *
from tkinter import colorchooser


class WhiteBoardApp(Tk):
    def __init__(self):
        super().__init__()
        
        self.title('WhiteBoardApp')
        self.geometry('1200x600')
        
        self.canvas = Canvas(self,
                             bg='white',
                             bd=0,
                             highlightthickness=0)
        self.canvas.pack(fill='both', expand=True)

        self.create_ui()

    def create_ui(self):
        frame = Frame(self,
                      bg='#252627',
                      bd=5,
                      relief=GROOVE)
        frame.pack(side='top',fill='x', padx=20, pady=10)
        
        self.color_button = Button(frame,
                                   text='Change Color',
                                   font=('Arial', 12),
                                   bg='#33A1FD',
                                   fg='#FFFAFB',
                                   bd=3,
                                   relief=RAISED,
                                   padx=5,
                                   pady=5).grid(row=0,column=0, padx=10, pady=10)
        
        self.clear_button = Button(frame,
                                   text='Clear Canvas',
                                   font=('Arial', 12),
                                   bg='#33A1FD',
                                   fg='#FFFAFB',
                                   bd=3,
                                   relief=RAISED,
                                   padx=5,
                                   pady=5).grid(row=0,column=1, padx=10, pady=10)

        self.pen_button = Button(frame,
                                   text='Pen (P)',
                                   font=('Arial', 12),
                                   bg='#33A1FD',
                                   fg='#FFFAFB',
                                   bd=3,
                                   relief=RAISED,
                                   padx=5,
                                   pady=5).grid(row=0,column=2, padx=10, pady=10)

        self.eraser_button = Button(frame,
                                   text='Eraser (E)',
                                   font=('Arial', 12),
                                   bg='#33A1FD',
                                   fg='#FFFAFB',
                                   bd=3,
                                   relief=RAISED,
                                   padx=5,
                                   pady=5).grid(row=0,column=3, padx=10, pady=10)

        
        Label(frame,
              text='Line Width:',
              font=('Arial', 12),
              bg='#252627',
              fg='#FFF9FB').grid(row=0, column=4, padx=10, pady=10)
        
        Scale(frame,
              from_=0,
              to=10,
              orient=HORIZONTAL,    # Orientation of scale
			  length=300,  # Length of the scale
              showvalue=1,  # Show the selected value on the scale,  If 0 hide current value
              tickinterval=20,  # Interval between ticks
              resolution=1,  # Resolution of the scale
              sliderlength=25,  # Length of the slider
              bg="lightgray",  # Background color
              fg="blue" ).grid(row=0, column=5, padx=10, pady=10)


if __name__ == '__main__':
    app = WhiteBoardApp()
    app.mainloop()
