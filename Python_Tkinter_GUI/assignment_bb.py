from tkinter import *
from tkinter import ttk


class StudentInformation(Tk):
    def __init__(self):
        super().__init__()

        self.title('StudentInformation')
        self.createUI()

    def save_text(self):
        student_info = (f"Student ID: {self.Id_entry.get()}\n"
                    f"First Name: {self.first_name_entry.get()}\n"
                    f"Last Name: {self.last_name_entry.get()}\n"
                    f"Programme: {self.programme_combo.get()}\n"
                    f"Gender: {self.gender_var.get()}\n"
                    f"Birthday: {self.day_var.get()} {self.month_var.get()} {self.year_var.get()}\n\n")

        self.info_text.insert(END, student_info)
 
    def createUI(self):

        Label(self,
              text='StudentInformation',
              font=('Arial', 15, 'bold'),
              fg='#FFFFFF',
              bg='#00A8E8',
              relief=RAISED,
              bd=7,
              padx=10,
              pady=5).grid(row=0, column=0, columnspan=4, padx=10, pady=20)

        # Student Id
        Label(self,
              text='Student Id:',
              font=('Arial', 12)).grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.Id_entry = Entry(self,
                         font=('Arial', 12))
        self.Id_entry.grid(row=1, column=1, padx=10, pady=10, sticky='w')
        
        # Name
        Label(self,
              text='First Name:',
              font=('Arial', 12)).grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.first_name_entry = Entry(self,
                         font=('Arial', 12))
        self.first_name_entry.grid(row=2, column=1, padx=10, pady=10, sticky='w')

        Label(self,
              text='Last Name:',
              font=('Arial', 12)).grid(row=3, column=0, padx=10, pady=10, sticky='w')
        self.last_name_entry = Entry(self,
                         font=('Arial', 12))
        self.last_name_entry.grid(row=3, column=1, padx=10, pady=10, sticky='w')
        
        # Programme
        Label(self,
              text='Programme:',
              font=('Arial', 12)).grid(row=4, column=0, padx=10, pady=10, sticky='w')
        self.programme_combo = ttk.Combobox(self,
                                       font=('Arial', 12),
                                       values=[
                                           'CSE',
                                           'Data Science',
                                           'EEE',
                                           'Others'
                                           ])
        self.programme_combo.grid(row=4, column=1, padx=10, pady=10, sticky='w')
        
        # Gender
        Label(self,
              text='Gender:',
              font=('Arial', 12)).grid(row=5, column=0, padx=10, pady=10, sticky='w')
        self.gender_var = StringVar(value='')

        male_radio = Radiobutton(self,
                                   font=('Arial', 12),
                                   variable=self.gender_var,
                                   text='Male',
                                   value='Male')
        male_radio.grid(row=5, column=1, padx=10, pady=10, sticky='w')

        female_radio = Radiobutton(self,
                                   font=('Arial', 12),
                                   variable=self.gender_var,
                                   text='Female',
                                   value='Female')
        female_radio.grid(row=5, column=2, padx=10, pady=10, sticky='w')

        other_radio = Radiobutton(self,
                                   font=('Arial', 12),
                                   variable=self.gender_var,
                                   text='Others',
                                   value='Others')
        other_radio.grid(row=5, column=3, padx=10, pady=10, sticky='w')

        # BirthDate
        Label(self,
              text='Birthday:',
              font=('Arial', 12)).grid(row=6, column=0, padx=10, pady=10, sticky='w')
        
        self.day_var = StringVar()
        day_combo = ttk.Combobox(self,
                                 font=('Arial', 12),
                                 textvariable=self.day_var,
                                 values=list(range(1, 32)))
        day_combo.grid(row=6, column=1, padx=10, pady=10, sticky='w')
        self.month_var = StringVar()
        month_combo = ttk.Combobox(self,
                                 font=('Arial', 12),
                                 textvariable=self.month_var,
                                 values=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
        month_combo.grid(row=6, column=2, padx=10, pady=10, sticky='w')
        
        self.year_var = StringVar()
        year_combo = ttk.Combobox(self,
                                 font=('Arial', 12),
                                 textvariable=self.year_var,
                                 values=list(range(1990, 2020)))
        year_combo.grid(row=6, column=3, padx=10, pady=10, sticky='w')
        
        # Submit
        Button(self,
                text='Submit',
                font=('Arial', 12, 'bold'),
                relief=GROOVE,
                borderwidth=10,
                bd=5,
                padx=10,
                pady=5,
                bg='#006992',
                fg='#EAF8BF',
                command=self.save_text).grid(row=7, column=0, columnspan=4, padx=10, pady=10)

        # Text
        self.info_text = Text(self,
            height=15,
            width=40,
            fg='#070600',
            bg='#F7F7FF',
            font=('Arial', 12),
            relief=GROOVE,
            bd=3,
            padx=10,
            pady=5)
        self.info_text.grid(row=8, column=0, columnspan=4, padx=10, pady=10)
        
        scrollbar = ttk.Scrollbar(self,
                              command=self.info_text.yview,
                              orient=VERTICAL)
        scrollbar.grid(row=8, column=4, sticky='ns')
        self.info_text.config(yscrollcommand=scrollbar.set)


if __name__ == '__main__':
    window = StudentInformation()
    window.mainloop()
