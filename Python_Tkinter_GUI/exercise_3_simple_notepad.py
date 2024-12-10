from tkinter import *
from tkinter import filedialog

def new_file():
    text.delete('1.0', END)

def open_file():
    filepath = filedialog.askopenfilename()
    with open(filepath, 'r') as file:
        text.delete('1.0', END)
        text.insert('1.0', str(file.read()))

def save_file():
    file = filedialog.asksaveasfile(defaultextension = '.txt',
                                    filetypes = [
                                        ("Text file",".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", ".*")
                                        ])
    if file:
        file_text = str(text.get('1.0', END))
        file.write(file_text)
        file.close()

def cut_text():
    selected_text = text.get(SEL_FIRST, SEL_LAST)
    text.delete(SEL_FIRST, SEL_LAST)
    window.clipboard_clear()
    window.clipboard_append(selected_text)

def copy_text():
    selected_text = text.get(SEL_FIRST, SEL_LAST)
    window.clipboard_clear()
    window.clipboard_append(selected_text)

def paste_text():
    text_paste = window.clipboard_get()
    text.insert(INSERT, text_paste)

def quit_app():
    window.quit()

window = Tk()
window.geometry('800x700')


# Create a menu
menubar = Menu(window)

# Create a file menu
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit_app)
menubar.add_cascade(label="File", menu=file_menu)


# Create an "Edit" menu
edit_menu = Menu(menubar, tearoff=0)
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)
menubar.add_cascade(label="Edit", menu=edit_menu)

# Add the menu to the root window
window.config(menu=menubar)

label = Label(window,
              text='Notepad',
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

window.mainloop()
