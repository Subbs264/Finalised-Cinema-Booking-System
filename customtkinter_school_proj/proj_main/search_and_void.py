import customtkinter as ctk
from credential_database import credential_connect

class BookingSearch(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Booking Search')
        self.geometry('600x480')

        self.label()
        self.entry()
        self.text()
        self.find_booking_button()
        self.terminate_booking_button()

    def label(self):
        self.title_label = ctk.CTkLabel(self, text='Bookings search', font=('Arial', 20))
        self.title_label.place(relx=0.5, rely=0.1, anchor='center')

    def entry(self):
        self.enter_phone = ctk.CTkEntry(self, placeholder_text='Enter Phone number', font=('Arial', 15), width=150)
        self.enter_phone.place(relx=0.5, rely=0.3, anchor='center')

    def text(self):
        self.text_box = ctk.CTkTextbox(self, width=400, height=200, font=('Arial', 14), state='disabled')
        self.text_box.place(relx=0.5, rely=0.55, anchor='center')

    def find_booking_button(self):
        self.find = ctk.CTkButton(self, text='Find Booking', font=('Arial', 14), width=100, command=self.locate_booking)
        self.find.place(relx=0.72, rely=0.3, anchor='center')

    def terminate_booking_button(self):
        self.terminate = ctk.CTkButton(self, text='Terminate Booking', font=('Arial', 14), width=100, fg_color='red', text_color='black', command=self.terminate_booking)
        self.terminate.place(relx=0.5, rely=0.85, anchor='center')

    def locate_booking(self):
        self.phone = self.enter_phone.get().strip()

        self.text_box.configure(state='normal')
        self.text_box.delete('1.0', 'end')

        if not self.phone:
            self.text_box.insert('1.0', 'Please enter a phone number to begin to look for a booking')
            self.text_box.configure(state='disabled')
            return


        if self.phone == 'all':
            result = credential_connect('bookings', 'SELECT * FROM bookings', fetch_all=True)
            pairs = [f'{x[0]}, {x[2]}, night: {x[3]}' for x in result]

            self.text_box.insert('1.0', '\n'.join(pairs))
            self.text_box.configure(state='disabled')
            return


        result = credential_connect('bookings', f"SELECT * FROM bookings WHERE phone='{self.phone}'", fetch_all=True)

        if result:
            self.text_box.insert('1.0', f'Name: {result[0][0]}\nCustomer Type: {result[0][1]}\nPhone: {result[0][2]}\nNight: {result[0][3]}\nSeats: {result[0][4].split(',')}')
        else:
            self.text_box.insert('1.0', 'No booking found for that phone number')

        self.text_box.configure(state='disabled')

    def terminate_booking(self):
        self.text_box.configure(state='normal')
        result = credential_connect('bookings', f"DELETE FROM bookings WHERE phone='{self.phone}'", fetch_all=True)
        if result:
            self.text_box.insert('1.0', 'Booking terminated')
        else:
            self.text_box.insert('1.0', 'No Booking selected to be terminated.\n')
        
        self.text_box.configure(state='disabled')

        print(result)

        return

if __name__ == '__main__':
    app = BookingSearch()
    app.mainloop()
