from tkinter import *
from tkinter import filedialog

def open_file():
    filepath = filedialog.askopenfilename()
    with open(filepath, 'r') as file:

        text.delete('1.0', END)
        text.insert('1.0', str(file.read()))

window = Tk()
window.geometry('600x450')

label = Label(window,
              text='File!',
              font=('Arial', 15, 'bold'),
              fg='#FFFFFF',
              bg='#00A8E8',
              relief=RAISED,
              bd=7,
              padx=10,
              pady=5)
label.pack(pady=20)

text = Text(window,
            height=10,
            width=30,
            fg='#070600',
            bg='#F7F7FF',
            font=('Arial', 14),
            relief=GROOVE,
            bd=3,
            padx=10,
            pady=5)
text.pack(pady=10)

file_button = Button(window,
                text='Open',
                font=('Arial', 12, 'bold'),
                relief=GROOVE,
                borderwidth=10,
                bd=5,
                padx=10,
                pady=5,
                bg='#006992',
                fg='#EAF8BF',
                command=open_file)
file_button.pack()

window.mainloop()
