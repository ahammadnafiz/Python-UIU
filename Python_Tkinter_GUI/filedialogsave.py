from tkinter import *
from tkinter import filedialog


def save_file():
    file = filedialog.asksaveasfile(defaultextension='.txt',
                                    filetypes = [
                                        ("Text file",".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", ".*")
                                        ])
    file_text = str(text.get('1.0', END))
    file.write(file_text)
    file.close()


window = Tk()
window.geometry('800x700')


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
            height=20,
            width=60,
            fg='#070600',
            bg='#F7F7FF',
            font=('Arial', 14),
            relief=GROOVE,
            bd=3,
            padx=10,
            pady=5)
text.pack(pady=10)

file_button = Button(window,
                text='Save',
                font=('Arial', 12, 'bold'),
                relief=GROOVE,
                borderwidth=10,
                bd=5,
                padx=10,
                pady=5,
                bg='#006992',
                fg='#EAF8BF',
                command=save_file)
file_button.pack()



window.mainloop()
