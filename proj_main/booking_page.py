import customtkinter as ctk
from logic import discount, calculate_new_price, update_details
from emailer import email
from verifications import Checker

'''
This page handles the booking segment of the process
It collects relevant details such as name, customer type and phone number
Details such as the night being booked and seats are forwarded on from stage_view.py 
After this all details are stored into the bookings database
'''

class Booking(ctk.CTk):
    def __init__(self, seats, night, seat_price=10):
        super().__init__()
        self.night= night
        self.seats = seats
        self.per_seat_price = seat_price
        self.seat_price = len(seats) * seat_price
        self.new_price = self.seat_price

        self.title('Booking')
        self.geometry('400x400')

        self.booking_label()
        self.name_entry()
        self.customer_type()
        self.phone_entry()
        self.error_label()
        self.seats_booked()
        self.age_discount()
        self.enter_button()
        self.description()
        self.termination_button()

    def booking_label(self):
        self.label = ctk.CTkLabel(self, text='Enter Customer Booking Information', font=('Arial', 20))
        self.label.place(relx=0.5, rely=0.1, anchor='n')

    def name_entry(self):
        self.name_field = ctk.CTkEntry(self, placeholder_text='Enter Name...')
        self.name_field.place(relx=0.5, rely=0.3, anchor='center')

    def customer_type(self):
        self.cust_type = ctk.CTkEntry(self, placeholder_text='Enter Type...')
        self.cust_type.place(relx=0.5, rely=0.4, anchor='center')
        self.cust_type.bind('<KeyRelease>', lambda e: self.discount_price())

    def phone_entry(self):
        self.phone_number = ctk.CTkEntry(self, placeholder_text='Enter Phone Number...')
        self.phone_number.place(relx=0.5, rely=0.5, anchor='center')

    def termination_button(self):
        self.terminate_button = ctk.CTkButton(self, text='Terminate Booking', text_color='Black', fg_color='red', width=40, hover_color='dark red', command=self.quit)
        self.terminate_button.place(relx=0.65, rely=0.87, anchor='w')

    def error_label(self):
        '''In combination with show_error'''
        self.error = ctk.CTkLabel(self, text='', font=('Arial', 12), text_color='red')
        self.error.place(relx=0.5, rely=0.70, anchor='center')

    def show_error(self, message):
        '''In combination with error_label'''
        self.error.configure(text=message)

    def seats_booked(self):
        self.num_seats = len(self.seats)
        self.booked_seats = ctk.CTkLabel(self, text=f'Number of seats: {self.num_seats}\nPrice: £{self.seat_price}')
        self.booked_seats.place(relx=0.5, rely=0.75, anchor='center')

    def enter_button(self):
        self.enter_btn = ctk.CTkButton(self, text='Enter', width=20, command=self.enter_details)
        self.enter_btn.place(relx=0.5, rely=0.87, anchor='center')
    
    def description(self):
        content = 'Type: reg (regular), gov or staff\n Enter "admin" into all fields to block out seats for the performance'
        self.desc_label = ctk.CTkLabel(self, text=content, font=('Arial', 10), text_color='gray')
        self.desc_label.place(relx=0.5, rely=0.98, anchor='s')

#-------------------------------------------Discount Related Functions-------------------------------------------
    def age_discount(self):
        '''Checks if the checkbox is ticked, if so, it calls upon another helper function in order to discount price in real time '''
        self.discount_checked = ctk.BooleanVar(value=False)
        self.discount = ctk.CTkCheckBox(self, text='Below 16 or above 65?', variable=self.discount_checked, command=self.toggle_for_discount)
        self.discount.place(relx=0.5, rely=0.65, anchor='center')
        self.counter = ctk.CTkEntry(self, placeholder_text='No. of discounted people', width=180)
        self.counter.bind('<KeyRelease>', lambda e: self.discount_price())  # used ai to find out how to use this (updates the price value in the ui in real time)

    def toggle_for_discount(self):
        '''Applies discount if there is data inside the discount entry'''
        if self.discount_checked.get():
            self.counter.place(relx=0.5, rely=0.57, anchor='center')
        else:
            self.counter.place_forget()
        self.discount_price()

    def discount_price(self):
        '''Calls the discount function from logic to apply the discount'''
        if self.cust_type.get().strip().lower() in ('gov', 'governor', 'staff'):
            self.new_price = 0
        elif self.discount_checked.get():
            try:
                discounted = discount(self.counter.get(), self.num_seats)
            except ValueError:
                discounted = 0
            self.new_price = calculate_new_price(self.num_seats, discounted, self.per_seat_price)
        else:
            self.new_price = self.seat_price
        self.booked_seats.configure(text=f'Number of seats: {self.num_seats}\nPrice: £{self.new_price}')
#----------------------------------------------------------------------------------------------------------------

    def enter_details(self):
        name = self.name_field.get().strip().title()
        cust_type = self.cust_type.get().strip().title()
        phone = self.phone_number.get().strip()
        performance = self.night
        seats_str = ','.join(self.seats)
        price_paid = self.new_price
        
        verify = Checker(phone=phone, name=name, cust=cust_type)

        is_admin, _ = verify.check_admin()
        if is_admin:
            price_paid = 0
        else:
            valid, reason = verify.check_all()
            if not valid:
                self.show_error(reason)
                return
        

        self.show_error('')
        
        update_details(name=name, cust_type=cust_type, phone=phone, performance=performance, seats_str=seats_str, price_paid=price_paid)

        #   email(name=name, qr_filepath=qr_filepath)
        #   Requires real email credentials so I left this out, in practise emailer.py would have the required credentials/API stuff

        self.quit()

if __name__ == '__main__':
    app = Booking(['A1', 'A2', 'A3'], 1)
    app.mainloop()
