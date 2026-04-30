import qrcode
import os

'''
Creates qr code using the qrcode library to hold the customers data
would be sent out using emailer.py but it isnt, view emailer.py for more info
'''

def create_qr(name, cust_type, phone, performance, seats, price_paid):
    content = {
        'Name': name,
        'Customer Type': cust_type,
        'Phone': phone,
        'Performance': performance,
        'Booked Seats': seats,
        'Amount paid': price_paid
    }

    os.makedirs('QRCode', exist_ok=True)
    filepath = f'QRCode\\qrcode_{name}_{phone}.png'

    qr = qrcode.QRCode()
    qr.add_data(content) # type: ignore

    img = qr.make_image()
    img.save(filepath) # type: ignore
    print('QRCode generated successfuly')

    return filepath