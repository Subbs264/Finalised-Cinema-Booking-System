#   Variable lists

This file contains and defines key variables from each python file.

>[!NOTE]
I did use an AI to help me create the rest of the variable list after finishing stage_view.py

#   main.py
NONE

#   stage_view.py
self.night -> contains the chosen night  (1, 2, 3)
self.seats -> a dictionary that contains all the seats
self.chosen_seats -> a list of seat IDs the user has selected
self.seat_state -> a dictionary tracking whether each seat is booked (True/False)
self.go_forward -> True/False that decides if the program should continue to the next stage

#   booking_page.py
self.seats -> list of seat IDs forwarded from stage_view
self.night -> the chosen performance night
self.seat_price -> total price calculated from number of seats
self.new_price -> updated price after any discounts are applied
self.discount_checked -> boolean tracking whether the discount checkbox is ticked

#   stafflogin.py
self.logged_in -> boolean that tracks if the user has successfully logged in
self.username_field -> the username entry widget
self.password_field -> the password entry widget
self.error_box -> label that displays login error messages

#   descision.py
self.selection -> stores the chosen night number (1, 2, 3)
self.go_forward -> boolean that decides if the program should continue

#   components.py
night_choice -> the selected performance night passed between stages
chosen_seats -> list of seats selected by the user passed to the booking page
login_screen.logged_in -> checked to decide if the program should continue past login

#   credential_database.py
connection -> the sqlite3 database connection object
cursor -> the sqlite3 cursor used to execute queries
result -> the data returned from a database query

#   logic.py
discounted -> the number of seats eligible for a discount
occupied -> a set of all booked and selected seats combined
has_gap -> boolean indicating if a single seat would be left stranded
