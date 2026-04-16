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

    #----------------------------------Title Label----------------------------------
    def booking_label(self):
        self.label = ctk.CTkLabel(self, text='Enter Customer Booking Information', font=('Arial', 20))
        self.label.place(relx=0.5, rely=0.1, anchor='n')

    #----------------------------------Name Entry----------------------------------
    def name(self):
        self.name_field = ctk.CTkEntry(self, placeholder_text='Enter Name...')
        self.name_field.place(relx=0.5, rely=0.3, anchor='center')

    #----------------------------------Customer Type Entry----------------------------------
    def customer_type(self):
        self.cust_type = ctk.CTkEntry(self, placeholder_text='Enter Type...')
        self.cust_type.place(relx=0.5, rely=0.4, anchor='center')

    #----------------------------------Phone Entry----------------------------------
    def phone(self):
        self.phone_number = ctk.CTkEntry(self, placeholder_text='Enter Phone Number...')
        self.phone_number.place(relx=0.5, rely=0.5, anchor='center')

    #----------------------------------Seats Label----------------------------------
    def seats_booked(self):
        self.num_seats = len(self.seats)
        self.booked_seats = ctk.CTkLabel(self, text=f'Number of seats: {self.num_seats}\nPrice: £{self.seat_price}')
        self.booked_seats.place(relx=0.5, rely=0.75, anchor='center')

    #----------------------------------Discounts Age----------------------------------
    def age_discount(self):
        '''Checks if the checkbox is ticked, if so, it calls upon another helper function in order to discount price in real time '''
        self.discount_checked = ctk.BooleanVar(value=False)
        self.discount = ctk.CTkCheckBox(self, text='Below 16 or above 65?', variable=self.discount_checked, command=self.toggle_counter)
        self.discount.place(relx=0.5, rely=0.65, anchor='center')
        self.counter = ctk.CTkEntry(self, placeholder_text='No. of discounted people', width=180)
        self.counter.bind('<KeyRelease>', lambda e: self.discount_price())  # used ai to find out how to use this (updates the price value in the ui in real time)

    def toggle_counter(self):
        '''Applies discount if there is data inside the discount entry'''
        if self.discount_checked.get():
            self.counter.place(relx=0.5, rely=0.57, anchor='center')
        else:
            self.counter.place_forget()
        self.discount_price()

    def discount_price(self):
        '''Calls the discount function from logic to apply the discount'''
        if self.discount_checked.get():
            try:
                discounted = discount(self.counter.get(), self.num_seats)
            except ValueError:
                discounted = 0
            self.new_price = calculate_new_price(self.num_seats, discounted, self.per_seat_price)
        else:
            self.new_price = self.seat_price
        self.booked_seats.configure(text=f'Number of seats: {self.num_seats}\nPrice: £{self.new_price}')

    #----------------------------------Enter Button----------------------------------
    def enter_button(self):
        '''Enter Button'''
        self.enter_btn = ctk.CTkButton(self, text='Enter', width=20, command=self.enter_details)
        self.enter_btn.place(relx=0.5, rely=0.87, anchor='center')
    #----------------------------------Discount entry Age----------------------------------
    def discounted_ticket_counter(self):
        '''Discouted entry box'''
        self.counter = ctk.CTkEntry(self, placeholder_text='No. of discounted people', width=180)

    def enter_details(self):
        name = self.name_field.get().strip().title()
        cust_type = self.cust_type.get().strip().title()
        phone = self.phone_number.get().strip().title()
        performance = self.night
        seats_str = ','.join(self.seats)
        price_paid = self.new_price
        
        entries = (name, cust_type, phone)
        
        if check_admin(entries):
            price_paid = 0

        if cust_type in ('staff', 'gov', 'governor'):
            price_paid = 0
        
        for entry in entries:
            if not entry:
                return
            else:
                pass
        
        result = credential_connect('bookings', f"SELECT * FROM bookings where phone='{phone}'", fetch_all=True)

        if result:
            existing_seats = result[0][4]
            existing_price = float(result[0][5])
            total_seats = f'{existing_seats},{seats_str}'
            existing_price += price_paid
            credential_connect('bookings', f"UPDATE bookings SET seats_booked='{total_seats}', price_paid='{existing_price}' WHERE phone='{phone}'", fetch_all=False)
        else:
            credential_connect("bookings",
                               f"INSERT INTO bookings VALUES ('{name}', '{cust_type}', '{phone}', '{performance}', '{seats_str}', '{price_paid}')", fetch_all=False)

        qr_filepath = CreateQR(name=name, cust_type=cust_type, phone=phone, performance=performance, seats=seats_str, price_paid=price_paid)

        #email(name=name, qr_filepath=qr_filepath) This is the emailer, requires a real details to work so i have removed it in reality I would put in real details

        self.quit()

    def description(self):
        content = 'Type: reg (regular), gov or staff\nEnter "admin" into all fields to remove a seat if the performance requires'
        self.desc_label = ctk.CTkLabel(self, text=content, font=('Arial', 10), text_color='gray')
        self.desc_label.place(relx=0.5, rely=0.98, anchor='s')


if __name__ == '__main__':
    app = Booking(['A1', 'A2', 'A3'], 1)
    app.mainloop()