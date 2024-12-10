from tkinter import *
from tkinter.ttk import *
import time

def start():
    task = 10
    var = 0

    while var < task:
        time.sleep(0.5)
        bar['value'] += 10
        var += 1
        percent.set(f"{(var/task) * 100}%")
        window.update_idletasks()

window = Tk()
window.geometry('500x300')

Label(window,
      text='Progressbar',
      font=('Arial', 10, 'bold')).pack(pady=30)

bar = Progressbar(window,
                  orient=HORIZONTAL,
                  length=300)
bar.pack(pady=10)

percent = StringVar()

percentLabel = Label(window,
                     textvariable=percent).pack()

Button(window,
       text='Start',
       command=start).pack(pady=10)
window.mainloop()
