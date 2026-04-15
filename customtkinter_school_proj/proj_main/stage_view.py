import customtkinter as ctk
from logic import get_booked_seats, check_gap

'''
stage_view.py handles the generation of the 200 seats, since the generation of each seat does not involve the process/manipulation of data I left it in here
Additionally it blacks out any already booked seats (Green -> Available, Red -> Selected, Black -> Already booked)
'''


class Stage(ctk.CTk):
    def __init__(self, seat_price, night=None):
        super().__init__()
        self.night = night
        self.seat_price = seat_price
        self.chosen_seats = []
        self.go_forward = False

        self.title('Stage View')
        self.geometry('1050x600')

        self.stage_position()
        self.seating()
        self.mark_booked_seats()
        self.book_all_button()
        self.error_box()
        
#----------------------------------Create Stage----------------------------------
    def stage_position(self):
        '''Sets the stage on the window'''
        self.stage = ctk.CTkButton(self, width=800, state='disabled', text='STAGE', font=('Arial', 20), text_color='black')
        self.stage.place(relx=0.5, rely=0.9, anchor='center')

#----------------------------------Creates Seats----------------------------------
    def seating(self):
        '''Creates seats using a double for loop, new rows are created after 10 seats'''
        self.seats = {}
        self.seat_state = {}
        column_count = 0
        
        for character in reversed('ABCDEFGHIJ'):
            for x in range(20):
                seat_id = f'{character}{x + 1}'
                self.seat_state[seat_id] = False
                self.seats[seat_id] = ctk.CTkButton(self, text=seat_id, width=50, fg_color='green', command=lambda s=seat_id: self.book_seat(s))
                
                self.seats[seat_id].place(relx=0.0004 + (x % 20) * 0.05, rely=0.1 + column_count * 0.03)
                
                if x == 19:
                    column_count += 1
            
            column_count += 1

#----------------------------------Seat Booking logic----------------------------------
    def book_seat(self, seat_id):
        if self.seat_state[seat_id]:
            self.seat_state[seat_id] = False
            self.seats[seat_id].configure(fg_color='green')
            if seat_id in self.chosen_seats:
                self.chosen_seats.remove(seat_id)
        else:
            self.seat_state[seat_id] = True
            self.seats[seat_id].configure(fg_color='red')
            self.chosen_seats.append(seat_id)


        self.update_book_all_button()

#----------------------------------Booking button----------------------------------
    def book_all_button(self):
        '''Button that displays price of seats chosen'''
        self.book_button = ctk.CTkButton(self, text='Please book a seat', width=150, height=50, bg_color='gray', fg_color='gray', font=('Arial', 20), corner_radius=0, command=self.book)
        self.book_button.place(relx=0.98, rely=0.83, anchor='se')

#----------------------------------Helper function that updates booking function with new text----------------------------------
    def update_book_all_button(self):
        '''Function that updates the boking button with new prices each time a new seat is added'''
        booked_count = len(self.chosen_seats)
        self.total_price = self.seat_price * booked_count
        if self.total_price > 0:
            self.book_button.configure(text=f'Book Now\nTotal: £{self.total_price}')
        else:
            self.book_button.configure(text=f'Please book a seat')

#----------------------------------Confirmation Function----------------------------------
    def book(self):
        '''Confirms if whether the program should continue'''
        if not self.chosen_seats:
            return

        booked_seats = get_booked_seats(self.night)
        has_gap, seat = check_gap(self.chosen_seats, booked_seats)
        if has_gap:
            self.error.configure(text=f'Seat {seat} is left out (Because its a middle seat), please include the middle seat or differ your booking')
            return

        self.go_forward = True
        self.quit()

#----------------------------------Marks booked seats----------------------------------
    def mark_booked_seats(self):
        booked_seats = get_booked_seats(self.night)
        for seat_id in booked_seats:
            if seat_id in self.seats:
                self.seats[seat_id].configure(state='disabled', fg_color='black')
                self.seat_state[seat_id] = True

    def error_box(self):
        self.error = ctk.CTkLabel(self, text='', text_color='red', font=('Arial', 14))
        self.error.place(relx=0.5, rely=0.95, anchor='center')

if __name__ == '__main__':
    app = Stage(10, 1)
    app.mainloop()