import customtkinter as ctk
from logic import login_validate, select_creds

'''
Staff login just handles the staff login (Username: Staff, Password: 123),
performs some simple validation
'''

class Login(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Login')
        self.geometry('400x240')

        self.username_entry()
        self.password_entry()
        self.title_label()
        self.error_box_output()
        self.enter_button()

        self.logged_in = False

    def title_label(self):
        self.login_title = ctk.CTkLabel(self, text='Staff login', font=('Arial', 20))
        self.login_title.place(relx=0.5, rely=0.35, anchor='center')

    def username_entry(self):
        self.username_field = ctk.CTkEntry(self, placeholder_text='Enter username...')
        self.username_field.place(relx=0.5, rely=0.5, anchor='center')

    def password_entry(self):
        self.password_field = ctk.CTkEntry(self, placeholder_text='Enter password...', show='#')
        self.password_field.place(relx=0.5, rely=0.65, anchor='center')

    def error_box_output(self):
        self.error_box = ctk.CTkLabel(self, text='', font=('Arial', 12), text_color='red')
        self.error_box.place(relx=0.46, rely=0.77, anchor='e')

    def enter_button(self):
        self.enter_details_button = ctk.CTkButton(self, text='Enter', width=20, command=self.enter_details)
        self.enter_details_button.place(relx=0.68, rely=0.77, anchor='e')

    def enter_details(self):
        username = self.username_field.get()
        password = self.password_field.get()
        creds = select_creds()

        verified, reasoning = login_validate(username, password, creds)


        if not verified:
            self.error_box.configure(text=reasoning)
        else:
            self.logged_in = True
            self.quit()


if __name__ == '__main__':
    login_Screen = Login()
    login_Screen.mainloop()