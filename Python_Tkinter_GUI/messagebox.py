from tkinter import *
from tkinter import messagebox

def click():
    info = 'This is info Message'
    #messagebox.showinfo(title='Show', message=info)
    #messagebox.showwarning(title='Warning', message=info)
    #messagebox.showerror(title='Error', message=info)
    if messagebox.askokcancel(title='OK or Cancel', message=info):
        display.delete(0, END)
        display.insert(0, 'You did it')
    else:
        display.delete(0, END)
        display.insert(0, 'You are a virus')


window = Tk()
window.geometry('500x400')
label = Label(window,
              text='MessageBox!',
              font=('Arial', 15, 'bold'),
              fg='#DDFFF7',
              bg='#7392B7',
              relief=RAISED,
              bd=7,
              padx=10,
              pady=5
              )

label.pack(padx=40, pady=20)

display = Entry(window,
                font=('Arial', 20)
                )
display.pack(pady=10)

show_button = Button(window,
                font=('Arial', 12),
                bg='#DB504A',
                text='Show',
                fg='#FEF9FF',
                relief=RAISED,
                bd=5,
                padx=10,
                pady=5,
                command=click)
show_button.pack(pady=10)

window.mainloop()

# Utilizes the tkinter messagebox module for creating interactive dialog boxes.
# Syntax:
#   messagebox.ask<type>(title, message, **options)
#       - <type>: Type of dialog box ('ok', 'okcancel', 'yesno', etc.)
#       - title: Title of the dialog box.
#       - message: Message displayed in the dialog box.
#       - **options: Additional customization options (e.g., icon, parent window, default button).

# Common uses include:
#   1. Confirmation Dialogs:
#       - Ask users to confirm actions, such as deletions or critical operations.
#       Example: messagebox.askokcancel("Confirmation", "Are you sure you want to delete this file?")

#   2. Error Handling:
#       - Display error messages for exceptions or invalid inputs, providing guidance.
#       Example: messagebox.showerror("Error", "Invalid input. Please enter a valid value.")

#   3. Informational Messages:
#       - Inform users about system status, updates, or important notifications.
#       Example: messagebox.showinfo("Information", "Your settings have been saved successfully.")

#   4. Warning Messages:
#       - Alert users about potential risks or actions that may have unintended consequences.
#       Example: messagebox.showwarning("Warning", "This action cannot be undone. Proceed with caution.")

#   5. Exit Confirmation:
#       - Confirm with users before exiting the application to prevent accidental closure.
#       Example: messagebox.askyesno("Exit", "Are you sure you want to exit the application?")


