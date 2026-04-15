import customtkinter as ctk

class Choice(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Choice')
        self.geometry('400x240')

        self.title_label()
        self.booking_button()
        self.stats_button()

        self.choice = ''
    
    #----------------------------------Title Label----------------------------------
    def title_label(self):
        '''Creates Title label for the page'''
        self.login_title = ctk.CTkLabel(self, text='Booking or View Stats', font=('Arial', 20))
        self.login_title.place(relx=0.5, rely=0.35, anchor='center')

    #----------------------------------Booking Button----------------------------------
    def booking_button(self):
        '''Creates the booking button'''
        self.book_button = ctk.CTkButton(self, text='Continue with Booking', width=50, command=self.book_choice)
        self.book_button.place(relx=0.25, rely=0.55, anchor='center')

    #----------------------------------Stats Button----------------------------------
    def stats_button(self):
        '''Creates the Stats button'''
        self.stat_button = ctk.CTkButton(self, text='View performance Stats', width=50, command=self.stat_choice)
        self.stat_button.place(relx=0.75, rely=0.55, anchor='center')

    def stat_choice(self):
        self.choice='view_stats'
        print('view_stats')
        self.quit()
    
    def book_choice(self):
        self.choice='continue_with_booking'
        print('continue_with_booking')
        self.quit()


if __name__ == '__main__':
    app = Choice()
    app.mainloop()