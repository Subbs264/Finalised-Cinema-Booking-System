import qrcode
import os

'''
Creates qr code using the qrcode library to hold the customers data
would be sent out using emailer.py but it isnt, view emailer.py for more info
'''

def create_qr(name, cust_type, phone, performance, seats, price_paid, save):
    content = {
        'Name': name,
        'Customer Type': cust_type,
        'Phone': phone,
        'Performance': performance,
        'Booked Seats': seats,
        'Amount paid': price_paid
    }
    terms = (name, cust_type, phone)

    if all(x.strip().lower() == 'admin' for x in terms):
        return

    os.makedirs('QRCode', exist_ok=True)
    filepath = f'QRCode\\qrcode_{name}_{phone}_night{performance}.png'

    qr = qrcode.QRCode()
    qr.add_data(content) # type: ignore

    if save:
        img = qr.make_image()
        img.save(filepath) # type: ignore
        print('============================')
        print('QRCode generated successfuly')
        print('============================')

    return filepath
