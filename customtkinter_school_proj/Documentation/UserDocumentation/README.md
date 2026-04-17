#   Cinema booking system USER documentation

This file contains an Installation Guide,an Interaction guide and some basic FAQs

#   UserMaintainance/InstallationGuide

Installation Guide:
--------------------------------------------------------------------------------------------------------------------------------
> [!NOTE]
Steps 1-3 are optional but are good practise when it comes to programming as it prevents package version conflicts and other 
annoying issues.
Also ensures others can recreate the environment exactly as it was during creation.
Any commands given are enclosed within a <command>Command<command>
--------------------------------------------------------------------------------------------------------------------------------


1. Download the package from its onedrive location, extract this if it is a .zip file.
2. Create a virtual environment by entering the following command into the terminal:
    <command>python -m venv .venv<command>  (ENSURE YOU ARE IN THE FILE'S PWD)
3. Activate the .venv file by using the command <command>./.venv/Scripts/Activate.ps1<command> (Once activated you will see a (.venv) beside your terminal line)
4. Perform the <command>cd ..<command> command twice to ensure 
5. Install requirements via the command python -m pip install requirements.txt
6. Run the main.py file inside the directory proj_main


#   UserMaintainance/InteractionGuide
> [!NOTE]
I have not inputted a real email into the emailer, it holds a temporary fake email address


1. Run main.py, a window should pop up with allowing you to choose between booking or viewing performance stats
2. If booking: log in with your staff credentials (Username: Staff, Password: 123)
3. Select the night of the performance you wish to book (Night 1, 2 or 3)
4. Select your seats, already chosen seats are marked black, your currently selected seats are red and green seats are free (we encourage to not leave middle seats)
5. Enter the customer's details (name, customer type, phone number). Tick the discount checkbox if the customer is under 18 or over 65 and enter the number of discounted people
   Normal customers require the type field to be 'regular', 'govener' for govener and 'staff' for staff
6. Press Enter to confirm. A QR code ticket will be generated and emailed to the customer
7. If you need to block out seats, enter 'admin' into all fields — this sets the booking cost to £0
8. After booking is finalised the program closes. Run main.py to begin another booking


#   UserMaintainance/FAQs&TroubleShooting

Q: I am encountering a database error as soon as I run main.py, what should i do?
A: Un-comment the hashed out Initialise_DB() function of the bottom and run the credential_database.py file, after doing so re-comment the function.

Q: I am unable to leave a gap seat when making a booking, why is this, is it a bug?
A: No it is not a bug, it is an intentional design feature that prevents gap seats from 'infecting' the play leaving plenty of seats sparsley spaced.

Q: How will I recieve my booking electronically?
A: You will recieve a Google Email that contains a QRCode speecifying your unique booking.

Q: I have created the virtual environment (.venv) and I have ran the program, it has generated the qrcode despite the message appearing in the terminal
A: Check where you are executing the code from, you may be inside .venv\Scripts still, perform <command>cd ..<command> twice or until you are inside the main project folder
