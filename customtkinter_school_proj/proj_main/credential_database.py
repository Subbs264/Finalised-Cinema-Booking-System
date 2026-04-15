import sqlite3
import os

'''
Credential_database.py creates the databases when the program has been run for the first time
If the program has already been run it will locate and connect to the databases provided they are in the same directory as the scripts
This contains the function credential_connect which is highly utilised in many other scripts serving as the middle man between data transfers
'''

#----------------------------------Initialises Staff Database----------------------------------
def create_staff_credential():
    '''Creates Staff Database if it doesnt already exist'''
    connection = sqlite3.connect('databases/staff_credentials')
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS staff_credentials (username TEXT, password TEXT)')
    cursor.execute('SELECT COUNT(*) FROM staff_credentials')

    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO staff_credentials VALUES ('Staff', 123)")

    connection.commit()
    connection.close()

#----------------------------------Initialises Booking Database----------------------------------
def create_booking_table():
    '''Creates Booking Database if it doesnt already exist'''
    connection = sqlite3.connect('databases/bookings')
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS bookings (name TEXT, customer_type TEXT, phone TEXT, performance_date TEXT, seats_booked TEXT, price_paid TEXT)')

    connection.commit()
    connection.close()

#----------------------------------Database Connection Function----------------------------------
def credential_connect(table, command, fetch_all=False):
    '''Connects to database of choice, execute command of choice returns the result'''
    connection = sqlite3.connect(f'databases/{table}')
    cursor = connection.cursor()
    cursor.execute(command)

    if command.strip().lower().startswith(('insert', 'update', 'delete')):
        connection.commit()
        result = None
    else:
        if fetch_all:
            result = cursor.fetchall()
        else:
            result = cursor.fetchone()

    connection.close()
    return result


def initialise_DBs():
    os.makedirs('databases', exist_ok=True)
    create_staff_credential()
    create_booking_table()

#initialise_DBs()