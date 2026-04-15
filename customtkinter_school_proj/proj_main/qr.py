import qrcode
import os

def CreateQR(name, cust_type, phone, performance, seats, price_paid):
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
    qr.add_data(content)

    img = qr.make_image()
    img.save(filepath)
    print('QRCode generated successfuly')

    return filepath