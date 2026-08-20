from sys import hash_info
from tkinter import *
from logic import *
class Gui:
    def __init__(self:object, window)->None:
        '''
        Initiates the starting screen for the app
        First_name text with input widget
        Last_name text with input widget
        Pin_number text with input widget
        Search Button with commands
        Create Button with commands
        welcome and to do text to be modify when Search Button is clicked
        withdraw/deposit input, text, buttons modify when Search Button is clicked



        '''
        self.window = window

        # First name and input
        self.first_name = Frame(self.window,width=450,height=10)
        self.first_name_label = Label(self.first_name, text='First Name')
        self.first_name_label.pack(side='left')  # Pack the label first
        self.first_name_input = Entry(self.first_name)
        self.first_name_input.pack(padx=10, side='left')
        self.first_name.pack(anchor='w', padx=10, pady=10)

        # Last name and input
        self.last_name = Frame(self.window,width=450,height=10)
        self.last_name_label = Label(self.last_name, text='Last Name')
        self.last_name_label.pack(side='left')  # Pack the label first
        self.last_name_input = Entry(self.last_name)
        self.last_name_input.pack(padx=10, side='left')
        self.last_name.pack(anchor='w', padx=10, pady=10)

        # Pin and input
        self.pin_number = Frame(self.window,width=450,height=10)
        self.pin_number_label = Label(self.pin_number, text='Enter Pin')
        self.pin_number_label.pack(side='left')  # Pack the label first
        self.pin_number_input = Entry(self.pin_number, show="*")
        self.pin_number_input.pack(padx=10, side='left')
        self.pin_number.pack(anchor='w', padx=10, pady=10)
        #search Button
        self.search_create_button = Frame(self.window,width=450,height=10)
        self.search_info_button = Button(
            self.search_create_button,
            text="SEARCH",
            command=lambda: search_click(
                self,
                self.first_name_input.get(),
                self.last_name_input.get(),
                self.pin_number_input.get()
            )
        )
        self.create_info_button = Button(
            self.search_create_button,
            text="CREATE ACCOUNT",
            command=lambda: create_click(
                self,
                self.first_name_input.get(),
                self.last_name_input.get(),
                self.pin_number_input.get()
            )
        )
        self.search_info_button.pack(side='left')
        self.create_info_button.pack(side='left')
        self.search_create_button.pack(anchor='w',padx=10,pady=10)
        #welcome text
        self.welcome = Frame(self.window,width=450,height=10)
        self.welcome_text = Label(self.welcome, text='')
        self.welcome_text.pack(side='left')
        self.welcome.pack(anchor = 'w',padx= 10, pady= 10)
        #to do text
        self.to_do = Frame(self.window,width=450,height=10)
        self.to_do_text = Label(self.to_do, text='')
        self.to_do_text.pack(side='left')
        self.to_do.pack(anchor='w', padx=10, pady=1)
        #withdraw and deposit radio buttons
        self.radio_button = Frame(self.window,width=450,height=10)
        self.money_decision = StringVar(value="")
        self.withdraw_button = Radiobutton(self.radio_button, text = "Withdraw",variable=self.money_decision, value="Withdraw")
        self.deposit_button = Radiobutton(self.radio_button, text = "Deposit",variable=self.money_decision, value="Deposit")
        self.withdraw_button.pack(side='left')
        self.deposit_button.pack(padx=20,side='left')
        self.radio_button.pack_forget()
        #Deposit/Withdraw Amount
        self.money_amount = Frame(self.window,width=450,height=10)
        self.money_amount_label = Label(self.money_amount, text='Amount')
        self.money_amount_label.pack(side='left')  # Pack the label first
        self.money_amount_input = Entry(self.money_amount)
        self.money_amount_input.pack(side='left')
        self.money_amount.pack_forget()
        # total amount text
        self.total_amount = Frame(self.window,width=450,height=10)
        self.total_amount_text = Label(self.total_amount, text='Account Balance: Class Number')
        self.total_amount_text.pack(side='left')
        self.total_amount.pack_forget()
