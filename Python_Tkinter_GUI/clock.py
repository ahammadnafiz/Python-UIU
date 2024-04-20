from tkinter import *
import time

app_window = Tk()
app_window.title("Digital Clock")
app_window.geometry("500x150")
app_window.resizable(1,1)

text_font= ("Boulder", 68, 'bold')

frame = Frame(app_window)
frame.pack()

label = Label(frame, 
              font=text_font,)
label.pack(pady=30)

def digital_clock():
   time_live = time.strftime("%I:%M:%S")
   label.config(text=time_live)
   label.after(200, digital_clock)

digital_clock()
app_window.mainloop()
