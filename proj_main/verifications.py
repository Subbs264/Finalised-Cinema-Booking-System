import string

'''
This file contains a class that contains functions that check values
'''


LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
SYMBOLS = string.punctuation
NUMBERS = string.digits

class Checker:
    def __init__(self, phone: str, name: str, cust: str):
        self.phone = phone
        self.name = name
        self.cust = cust

        self.entries = (self.phone, self.name, self.cust)

    def presence_check(self):
        if not all(x for x in self.entries):
            return False, 'Please fill in all fields'
        return True, ''

    def check_admin(self):
        if all(x.lower() == 'admin' for x in self.entries):
            return True, 'admin'
        return False, ''

    def phone_number_check(self):
        self.phone = self.phone.strip()
        self.phone = self.phone.replace('+44', '0')
        phone = self.phone
        
        if len(phone) > 11 or len(phone) < 11:
            return False, 'Invalid number of digits'
        
        if any(x in LOWERCASE or x in UPPERCASE or x in SYMBOLS for x in phone):
            return False, 'Number given contains invalid characters'
        
        return True, ''

    def name_check(self):
        name = self.name.strip()

        if len(name) > 20:
            return False, 'Too many characters'
        
        if any(x in NUMBERS or x in SYMBOLS for x in name):
            return False, 'Invalid characters used'
        
        return True, ''

    def cust_type_check(self):
        cust = self.cust.strip().lower()
        types = ('staff', 'gov', 'governor', 'regular', 'reg')

        if cust not in types:
            return False, 'Customer Type unrecognised'
        
        if cust in types[2:]:
            return True, 'priority access'
        
        return True, ''


    def check_all(self):
        checks = {
            'presence': self.presence_check,
            'name': self.name_check,
            'phone': self.phone_number_check,
            'cust': self.cust_type_check,
        }

        for check_names, check in checks.items():
            validity, reasoning = check()
            if not validity:
                return False, reasoning

        return True, ''