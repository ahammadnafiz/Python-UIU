from tkinter import *

# Text widget = funtions like text area, you can enter multiple line of text

def save_text():
    user = text.get('1.0', END)
    print(user)

window = Tk()
window.geometry('800x700')

label = Label(window,
              text='Notepad!',
              font=('Arial', 15, 'bold'),
              fg='#FFFFFF',
              bg='#00A8E8',
              relief=RAISED,
              bd=7,
              padx=10,
              pady=5)
label.pack(pady=20)

text = Text(window,
            height=20,
            width=60,
            fg='#070600',
            bg='#F7F7FF',
            font=('Ink Free', 14),
            relief=GROOVE,
            bd=3,
            padx=10,
            pady=5)
text.pack(pady=10)

save = Button(window,
                text='Save',
                font=('Arial', 12, 'bold'),
                relief=GROOVE,
                borderwidth=10,
                bd=5,
                padx=10,
                pady=5,
                bg='#006992',
                fg='#EAF8BF',
                command=save_text)
save.pack(pady=10)

window.mainloop()
