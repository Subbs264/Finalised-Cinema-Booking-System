import customtkinter as ctk
from logic import pull_data

class stat_viewer(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Performance Stats')
        self.geometry('1200x600')

        self.revenue, self.seat_count = pull_data()

        self.title_label()

#-----------------------------------------Builds Content for the table displayed---------------------------------------------------

        self.content = {'Title 1': '', 'Title 2': 'Night 1', 'Title 3': 'Night 2', 'Title 4': 'Night 3',
                        'Total Revenue': f'Total Revenue: £{sum(self.revenue.values())}', 'rev_1': self.revenue[1], 'rev_2': self.revenue[2], 'rev_3': self.revenue[3],
                        'Total seats sold': f'Total Seats Sold: {sum(self.seat_count.values())}', 'seats_1': self.seat_count[1], 'seats_2': self.seat_count[2], 'seats_3': self.seat_count[3],
                        'Total seats remaining': f'Total Remaining: {600 - sum(self.seat_count.values())}', 'rem_1': 200 - self.seat_count[1], 'rem_2': 200 - self.seat_count[2], 'rem_3': 200 - self.seat_count[3]}

        for i, value in enumerate(self.content.values()):   # Did use a little bit of AI (line 22-25)
            x = i // 4
            y = i % 4
            self.label(x_pos=(0.2 + y * 0.2), y_pos=(0.2 + x * 0.1), text=value)

        
#-----------------------------------------Title Label---------------------------------------------------

    def title_label(self):
        '''Creates Title label for the stats page'''
        self.login_title = ctk.CTkLabel(self, text='Performance Stats', font=('Arial', 20))
        self.login_title.place(relx=0.5, rely=0.1, anchor='center')

#-----------------------------------------Label Template---------------------------------------------------
    def label(self, x_pos, y_pos, text):
        '''Template label created for later use'''
        self.show_data = ctk.CTkLabel(self, text=text, font=('Arial', 20))
        self.show_data.place(relx=x_pos, rely=y_pos, anchor='center')

if __name__ == '__main__':
    app = stat_viewer()
    app.mainloop()