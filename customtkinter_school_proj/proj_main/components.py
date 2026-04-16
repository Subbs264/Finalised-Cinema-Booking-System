from stafflogin import Login
from descision import Decision
from stage_view import Stage
from booking_page import Booking
from credential_database import initialise_DBs
from logic import price_checker
from choice import Choice
from stats import stat_viewer
from search_and_void import BookingSearch
'''
Components.py is the connective tissue of the project tieing the program together
It calls upon various functions from other files within the proj_main directory
'''

#----------------------------------Function that ties everything together----------------------------------
def run_program():
    initialise_DBs()

    choice_screen = Choice()
    choice_screen.mainloop()
    choice_screen.destroy()

    if not choice_screen.choice:
        return
    
    if choice_screen.choice == 'view_stats':
        stat_screen = stat_viewer()
        stat_screen.mainloop()
        stat_screen.destroy()
        return

    elif choice_screen.choice == 'terminate_booking':
        book_search = BookingSearch()
        book_search.mainloop()
        book_search.destroy()
        return

    login_screen = Login()
    login_screen.mainloop()
    login_screen.destroy()

    if not login_screen.logged_in:
        return

    night = Decision()
    night.mainloop()
    night_choice = night.selection
    night.destroy()

    if not night.go_forward:
        return

    seat_price = price_checker(night_choice)
    stage_view = Stage(seat_price=seat_price, night=night_choice)
    stage_view.mainloop()
    chosen_seats = stage_view.chosen_seats
    stage_view.destroy()

    if not stage_view.go_forward:
        return

    booking_page = Booking(chosen_seats, night_choice, seat_price=seat_price)
    booking_page.mainloop()
    booking_page.destroy()
    

if __name__ == '__main__':
    run_program()