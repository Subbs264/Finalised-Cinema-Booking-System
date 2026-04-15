import customtkinter as ctk
from credential_database import credential_connect
from logic import validate

'''
Staff login just handles the staff login (Username: Staff, Password: 123)
'''


class Login(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Login')
        self.geometry('400x240')

        self.username()
        self.password()
        self.title_label()
        self.error()
        self.enter_button()

        self.logged_in = False

#----------------------------------Title Label----------------------------------
    def title_label(self):
        '''Creates Title label Staff Login'''
        self.login_title = ctk.CTkLabel(self, text='Staff login', font=('Arial', 20))
        self.login_title.place(relx=0.5, rely=0.35, anchor='center')

#----------------------------------Username Entry----------------------------------
    def username(self):
        '''Creates username entry'''
        self.username_field = ctk.CTkEntry(self, placeholder_text='Enter username...')
        self.username_field.place(relx=0.5, rely=0.5, anchor='center')

#----------------------------------Password label----------------------------------
    def password(self):
        '''Creates Password entry'''
        self.password_field = ctk.CTkEntry(self, placeholder_text='Enter password...', show='#')
        self.password_field.place(relx=0.5, rely=0.65, anchor='center')

#----------------------------------Error Box label----------------------------------
    def error(self):
        '''Error box creations for future use'''
        self.error_box = ctk.CTkLabel(self, text='', font=('Arial', 12), text_color='red')
        self.error_box.place(relx=0.46, rely=0.77, anchor='e')

#----------------------------------Enter button----------------------------------
    def enter_button(self):
        '''Creates the enter buttn'''
        self.enter_details_button = ctk.CTkButton(self, text='Enter', width=20, command=self.enter_details)
        self.enter_details_button.place(relx=0.68, rely=0.77, anchor='e')

#----------------------------------Enter details, validations----------------------------------
    def enter_details(self):
        ''''Enter Details, validates them returns a response if not valid'''
        username = self.username_field.get()
        password = self.password_field.get()
        creds = credential_connect('staff_credentials', 'SELECT * FROM staff_credentials', fetch_all=False)

        verified, reasoning = validate(username, password, creds)

        if not verified:
            self.error_box.configure(text=reasoning)
        else:
            self.logged_in = True
            self.quit()


if __name__ == '__main__':
    login_Screen = Login()
    login_Screen.mainloop()