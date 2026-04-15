import customtkinter as ctk


'''
This is Decision.py, It simply is the interface where the chosen night of performance to view is selected
Apart from collecting the night number it doesnt really do much
'''



class Decision(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.selection = None
        self.go_forward = False

        self.title('Descision')
        self.geometry('400x240')

        self.buttons()
        self.label()
#----------------------------------Choose performance label----------------------------------
    def label(self):
        '''Option for which performance to choose'''
        self.label_field = ctk.CTkLabel(self, text='Choose which performance\n to view', font=('Arial', 20))
        self.label_field.place(relx=0.5, rely=0.3, anchor='center')

#----------------------------------Create buttons corresponding to night----------------------------------
    def buttons(self):
        '''Creates buttons that allow user to select night'''
        positions = {0.25: 1, 0.5: 2, 0.75: 3}
        for position, text in positions.items():
            self.night_button = ctk.CTkButton(self, text=f'Night {text}', width=50, command=lambda t=text: self.take_to_performance(t))
            self.night_button.place(relx=position, rely=0.55, anchor='center')

#----------------------------------Function that makes self.go_forward True----------------------------------
    def take_to_performance(self, night):
        '''Decides whether program sould continue onto the next stage'''
        self.selection = night
        self.go_forward = True
        self.quit()



if __name__ == '__main__':
    app = Decision()
    app.mainloop()