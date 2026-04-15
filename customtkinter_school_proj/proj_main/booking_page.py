import customtkinter as ctk
from credential_database import credential_connect
from logic import discount, calculate_new_price, check_admin
from qr import CreateQR
from emailer import email

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
        self.name()
        self.customer_type()
        self.phone()
        self.seats_booked()
        self.age_discount()
        self.enter_button()
        self.description()

    def booking_label(self):
        self.label = ctk.CTkLabel(self, text='Enter Customer Booking Information', font=('Arial', 20))
        self.label.place(relx=0.5, rely=0.1, anchor='n')

    def name(self):
        self.name_field = ctk.CTkEntry(self, placeholder_text='Enter Name...')
        self.name_field.place(relx=0.5, rely=0.3, anchor='center')

    def customer_type(self):
        self.cust_type = ctk.CTkEntry(self, placeholder_text='Enter Type...')
        self.cust_type.place(relx=0.5, rely=0.4, anchor='center')

    def phone(self):
        self.phone_number = ctk.CTkEntry(self, placeholder_text='Enter Phone Number...')
        self.phone_number.place(relx=0.5, rely=0.5, anchor='center')

    def seats_booked(self):
        self.num_seats = len(self.seats)
        self.booked_seats = ctk.CTkLabel(self, text=f'Number of seats: {self.num_seats}\nPrice: £{self.seat_price}')
        self.booked_seats.place(relx=0.5, rely=0.75, anchor='center')

    def age_discount(self):
        self.discount_checked = ctk.BooleanVar(value=False)
        self.discount = ctk.CTkCheckBox(self, text='Below 18 or above 65?', variable=self.discount_checked, command=self.toggle_counter)
        self.discount.place(relx=0.5, rely=0.65, anchor='center')
        self.counter = ctk.CTkEntry(self, placeholder_text='No. of discounted people', width=180)
        self.counter.bind('<KeyRelease>', lambda e: self.discount_price())  # used ai to find out how to use this (updates the price value in the ui in real time)

    def toggle_counter(self):
        if self.discount_checked.get():
            self.counter.place(relx=0.5, rely=0.57, anchor='center')
        else:
            self.counter.place_forget()
        self.discount_price()

    def discount_price(self):
        if self.discount_checked.get():
            try:
                discounted = discount(self.counter.get(), self.num_seats)
            except ValueError:
                discounted = 0
            self.new_price = calculate_new_price(self.num_seats, discounted, self.per_seat_price)
        else:
            self.new_price = self.seat_price
        self.booked_seats.configure(text=f'Number of seats: {self.num_seats}\nPrice: £{self.new_price}')

    def enter_button(self):
        self.enter_btn = ctk.CTkButton(self, text='Enter', width=20, command=self.enter_details)
        self.enter_btn.place(relx=0.5, rely=0.87, anchor='center')

    def discounted_ticket_counter(self):
        self.counter = ctk.CTkEntry(self, placeholder_text='No. of discounted people', width=180)

    def enter_details(self):
        name = self.name_field.get()
        cust_type = self.cust_type.get()
        phone = self.phone_number.get()
        performance = self.night
        seats_str = ','.join(self.seats)
        price_paid = self.new_price
        
        entries = (name, cust_type, phone)
        
        if check_admin(entries):
            price_paid = 0
        
        for entry in entries:
            if not entry:
                return
            else:
                pass

        credential_connect("bookings",
                           f"INSERT INTO bookings VALUES ('{name}', '{cust_type}', '{phone}', '{performance}', '{seats_str}', '{price_paid}')", fetch_all=False)

        qr_filepath = CreateQR(name=name, cust_type=cust_type, phone=phone, performance=performance, seats=seats_str, price_paid=price_paid)

        email(name=name, qr_filepath=qr_filepath)

        self.quit()

    def description(self):
        content = 'Type: reg (regular), gov or staff\nEnter "admin" into all fields to remove a seat if the performance requires'
        self.desc_label = ctk.CTkLabel(self, text=content, font=('Arial', 10), text_color='gray')
        self.desc_label.place(relx=0.5, rely=0.98, anchor='s')


if __name__ == '__main__':
    app = Booking([1, 2, 3, 4, 5], 1)
    app.mainloop()