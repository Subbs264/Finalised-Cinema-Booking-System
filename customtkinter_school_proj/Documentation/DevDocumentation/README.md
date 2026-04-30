#   Cinema booking system DEVELOPER documentation

This file contains the paths to various useful files that will help future developers to build upon, maintain and/or improve

#   DevMaintainance/UsefulFiles

Hello there developer, I have included a variable list and a data dictionary for better understanding of how the program works.
In addition to this I have drawn out a 2 basic flow charts to demonstrate the schematics of the 2, what I think are the most important files.
All relevant files can be found in Documentation/DevDocumentation.

I created the flow chart files in a website called (https://app.diagrams.net/), upload the following 2 .drawio files into this to view them

#   File Overview

| File                  | Purpose                                                                 |
|-----------------------|-------------------------------------------------------------------------|
| main.py               | Entry point, calls run_program()                                        |
| components.py         | Ties all windows together, controls program flow                        |
| choice.py             | First screen — lets staff choose between booking or viewing stats       |
| stafflogin.py         | Staff login screen                                                      |
| descision.py          | Night selection screen (Night 1, 2 or 3)                                |
| stage_view.py         | Seat selection screen with 200-seat grid                                |
| booking_page.py       | Customer details entry and booking confirmation                         |
| stats.py              | Stats viewer showing revenue and seats sold per night                   |
| logic.py              | All data processing — pricing, discounts, validation, gap checking      |
| credential_database.py| Database connection handler for bookings and staff credentials          |
| qr.py                 | Generates a QR code image containing booking details                    |
| emailer.py            | Sends the QR code ticket to the customer via Gmail SMTP                 |