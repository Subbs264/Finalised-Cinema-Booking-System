from credential_database import credential_connect

''''
Logic.py contains all necessary data manipulations helper functions seperating the data processing and handling from the designated UI files
I have mainly commented on these functions as they are not as understandable as they have little context surrounding them
'''

#----------------------------------Dynamic pricing based on seats sold----------------------------------
def price_checker(night, base_price=10, total_seats=200):
    '''Adjusts seat price based on how full the performance is'''
    booked = len(get_booked_seats(night))
    percent_sold = booked / total_seats

    if percent_sold >= 0.8:
        return round(base_price * 1.5)
    elif percent_sold >= 0.6:
        return round(base_price * 1.25)
    elif percent_sold >= 0.4:
        return base_price
    elif percent_sold >= 0.2:
        return round(base_price * 0.9)
    else:
        return round(base_price * 0.8)

#----------------------------------Discount Function----------------------------------
def discount(counter, seats):
    '''Returns the number of discounted seats, also capping it to prevent price from dropping below what it should'''
    return min(int(counter), seats)

#----------------------------------Calculates new price----------------------------------
def calculate_new_price(seats, discounted_price, seat_price=10):
    '''Calculates the total price of seats (seat_price for every standard one, under half for every discounted one)'''
    return (((seats - discounted_price) * seat_price) + (discounted_price * (seat_price // 2 - 1)))

#----------------------------------Checks to see if admin is blocking seats----------------------------------
def check_admin(entries):
    '''Checks whether all inputs are admin, if so seat prices are reduced to 0 (returns True/False)'''
    return all(entries[i].lower() == 'admin' for i in range(3))

#----------------------------------Common validation techniques----------------------------------
def validate(username, password, creds):
    '''Login validation with reasoning repsonses'''
    if not username:
        return False, 'Enter username'
        
    if not password:
        return False, 'Enter password'
    
    if username == creds[0] and password == str(creds[1]):
        return True, ''
    else:
        return False, 'Incorrect credentials'
    
#----------------------------------Checks for middle seats----------------------------------
def check_gap(chosen_seats, booked_seats, rows='ABCDEFGHIJ', cols=20):
    '''Returns True if booking these seats would leave a single empty seat stranded between occupied seats in any row'''
    occupied = set(chosen_seats) | set(booked_seats)    # combines sets

    for row in rows:
        for col in range(1, cols + 1):
            seat = f'{row}{col}'
            if seat in occupied:
                continue

            left_seat_occupied = col == 1 or f'{row}{col - 1}' in occupied
            right_seat_occupied = col == cols or f'{row}{col + 1}' in occupied

            if left_seat_occupied and right_seat_occupied:
                return True, seat

    return False, None

#----------------------------------Pulls revenue and seat count per night----------------------------------
def pull_data():
    '''Returns revenue and seat count dictionaries for all 3 nights'''
    result = credential_connect('bookings', 'SELECT performance_date, seats_booked, price_paid FROM bookings', fetch_all=True)

    revenue = {1: 0, 2: 0, 3: 0}
    seat_count = {1: 0, 2: 0, 3: 0}

    for night, seats, price in result:
        night = int(night)
        revenue[night] += float(price)
        seat_count[night] += len(seats.split(','))

    return revenue, seat_count

#----------------------------------Unpacks data for Booking_page----------------------------------
def get_booked_seats(night):
    '''Grabs bookings from database and returns a clean list of seats booked on the given night'''
    bookings = credential_connect('bookings', 'SELECT performance_date, seats_booked FROM bookings', fetch_all=True)

    if not bookings:
        return []
    else:
        booked = []

        for performance, string_seats in bookings:
            if str(performance) == str(night):
                booked.extend(string_seats.split(','))

        return [seats.strip() for seats in booked]