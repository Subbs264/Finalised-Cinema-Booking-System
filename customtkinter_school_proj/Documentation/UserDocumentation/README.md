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

1. Run main.py a window should pop up, requesting a username/password (Username, Password = STAFF, 123)
2. Follow on screen instructions, selecting a night
3. Select your seats, already chosen seats will be coloured black, currently chosen seats (yours) are highlighted red, once seats are chosen select the book seats button
4. Once seats are chosen, input the customers details and finalise the bookings/ If you are looking to block out seats input admin into every entry to nullify the booking cost
5. After booking is finalised the program shuts down, saving the saved details, run main.py to begin another booking


#   UserMaintainance/FAQs&TroubleShooting

Q: I am encountering a database error as soon as I run main.py, what should i do?
A: Un-comment the hashed out Initialise_DB() function of the bottom and run the credential_database.py file, after doing so re-comment the function.

Q: I am unable to leave a gap seat when making a booking, why is this, is it a bug?
A: No it is not a bug, it is an intentional design feature that prevents gap seats from 'infecting' the play leaving plenty of seats sparsley spaced.

Q: How will I recieve my booking electronically?
A: You will recieve a Google Email that contains a QRCode speecifying your unique booking.
