from tkinter import *

count = 0

def increase_count():
    global count
    count += 1
    entry.delete(0, END)
    entry.insert(0, str(count))

def decrease_count():
    global count
    if count == 0:
        count = 0
        entry.delete(0, END)
        entry.insert(0, str(count))
    else:
        count -= 1
        entry.delete(0, END)
        entry.insert(0, str(count))


window = Tk()
window.geometry('440x350')

label = Label(window,
              text='Tosbi Counter!',
              font=('Arial', 20, 'bold'),
              fg='#232528',
              bg='#61E786',
              relief=RAISED,
              bd=7,
              padx=10,
              pady=5)
label.pack(padx=40, pady=20)

entry = Entry(window)
entry.pack(pady=10)

entry.configure(width=25,
                font=('Helvetica', 16))


increase = Button(window, 
                  text='Increase', 
                  font=('Arial', 15, 'bold'),
                  command=increase_count)
increase.pack(padx=30, pady=10)

decrease = Button(window, 
                  text='Decrease', 
                  font=('Arial', 15, 'bold'),
                  command=decrease_count)
decrease.pack(padx=60, pady=10)

window.mainloop()
