from tkinter import * 
from tkinter import ttk


window = Tk()
window.geometry('500x500')

style = ttk.Style()
style.configure('Notebook.Tab', background='lightblue', foreground='darkblue', padding=[10, 5])

# Creating ttk.notebook Widget
notebook = ttk.Notebook(window) # Widget that manages a collection of window/display

# Creating tabs/pages
tab1 = Frame(notebook)
tab2 = Frame(notebook)

# Adding tabs to the notebook
notebook.add(tab1, text = 'Tab 1')
notebook.add(tab2, text = 'Tab 2')
notebook.pack(fill='both', expand=True)

# Adding contents to the tabs
Label(tab1, text='This is Tab 1',
      font=('Arial', 15, 'bold'),
              fg='#FFFFFF',
              bg='#00A8E8',
              relief=RAISED,
              bd=7,
              padx=10,
              pady=5).pack(pady=50)
Label(tab2, text='This is Tab 2',
      font=('Arial', 15, 'bold'),
              fg='#FFFFFF',
              bg='#00A8E8',
              relief=RAISED,
              bd=7,
              padx=10,
              pady=5).pack(pady=50)

window.mainloop()

