import csv
import os
from gui import *


def search_click(gui: object, first_name: str, last_name: str, pin: str) -> None:
    """
    Handles the search functionality for an account.

    Inputs are gather from GUI
    This code will raise Errors if any of the inputs are empty
    or if all information is entered but information incorrect,
    that will raise an error
    When valid adds all buttons and text to enter or restart.

    Raises:
        ValueError: If any input field is empty.
    """
    try:
        if not first_name.strip():
            raise ValueError("Enter first name.")
        if not last_name.strip():
            raise ValueError("Enter last name.")
        if not pin.strip():
            raise ValueError("Enter a Pin.")

        with open("data.csv", mode="r", newline="") as file:
            reader = csv.reader(file)
            found = False
            for row in reader:
                if len(row) >= 3 and row[0] == first_name and row[1] == last_name and row[2] == pin:
                    account_balance = round(float(row[3]), 2)
                    gui.welcome_text.config(
                        text=f"Welcome {first_name} {last_name}. Account Balance: {account_balance:.2f}", fg="green")
                    gui.to_do_text.config(text="What would you like to do?", fg="green")
                    gui.radio_button.pack(anchor='w', padx=10, pady=10)
                    gui.money_amount.pack(anchor='w', padx=10, pady=10)

                    # Create buttons
                    gui.entry_exit = Frame(gui.window, width=450, height=10)
                    gui.enter_box = Button(
                        gui.entry_exit,
                        text="ENTER",
                        command=lambda: enter_click(
                            gui,
                            gui.money_amount_input.get(),
                            gui.money_decision.get(),
                            account_balance,
                            first_name,
                            last_name,
                            pin
                        )
                    )
                    gui.exit_box = Button(gui.entry_exit, text="EXIT", command=lambda: restart(gui))
                    gui.enter_box.pack(side='left')
                    gui.exit_box.pack(padx=30, side='left')
                    gui.entry_exit.pack(anchor='w', padx=10, pady=10)
                    gui.to_do_text.pack(anchor='w', padx=10, pady=10)
                    gui.welcome_text.pack(anchor='w', padx=10, pady=10)
                    gui.search_create_button.pack_forget()
                    gui.pin_number.pack_forget()
                    gui.first_name.pack_forget()
                    gui.last_name.pack_forget()

                    found = True
                    return

            if not found:
                gui.welcome_text.config(text="Invalid information, please try again.", fg="red")

    except ValueError as e:
        gui.welcome_text.config(text=str(e), fg="red")


def enter_click(gui: object, amount: str, bank_action: str, balance: float, first_name: str, last_name: str,
                pin: str) -> None:
    """
    Handles the 'Enter' button click.

    Inputs are gather from GUI
    If the inputs are empty, it will tell the user to
    select a bank function
    It will proceed to withdraw/deposit process if something is filled
    """
    if not gui.money_decision.get():
        gui.total_amount.pack(anchor='w', padx=10, pady=10)
        gui.total_amount_text.config(text="Choose a Function: Withdraw or Deposit", fg="red")
    else:
        withdraw_deposit(gui, amount, bank_action, balance, first_name, last_name, pin)


def withdraw_deposit(gui: object, amount: str, bank_action: str, current_balance: float, first_name: str,
                     last_name: str, pin: str) -> None:
    """
    Handles withdrawing or depositing money.

    Checks if the amount of money is a float
    Raises Error if value is negative, not a float,
    or exceeds the current balance if user selected withdraw
    After getting a valid input, it proceeds to update.
    """
    try:
        amount = round(float(amount), 2)
    except ValueError:
        gui.total_amount.pack(anchor='w', padx=10, pady=10)
        gui.total_amount_text.config(text="Please enter a valid number.", fg="red")
        return

    if amount <= 0:
        gui.total_amount.pack(anchor='w', padx=10, pady=10)
        gui.total_amount_text.config(text="Please enter a positive number.", fg="red")
        return

    if amount > current_balance and bank_action == "Deposit":
        update(gui, amount, bank_action, current_balance, first_name, last_name, pin)
        return

    if amount > current_balance:
        gui.total_amount.pack(anchor='w', padx=10, pady=10)
        gui.total_amount_text.config(text="Value exceeds your current balance", fg="red")
        return

    update(gui, amount, bank_action, current_balance, first_name, last_name, pin)


def update(gui: object, amount: float, bank_action: str, current_balance: float, first_name: str, last_name: str,
           pin: str) -> None:
    """
    Updates the account balance after a transaction.

    get rids of entry button
    welcome text
    radio buttons
    money amount entry
    The only thing left would total amount text and exit button.
    """
    if bank_action == "Withdraw":
        current_balance -= amount
        gui.total_amount.pack(anchor='w', padx=10, pady=10)
        gui.total_amount_text.config(text=f"Withdrawn {amount:.2f}. New Balance: {current_balance:.2f}", fg="green")
    elif bank_action == "Deposit":
        current_balance += amount
        gui.total_amount.pack(anchor='w', padx=10, pady=10)
        gui.total_amount_text.config(text=f"Deposited {amount:.2f}. New Balance: {current_balance:.2f}", fg="green")
    gui.welcome_text.pack_forget()
    gui.to_do_text.pack_forget()
    gui.enter_box.pack_forget()
    gui.radio_button.pack_forget()
    gui.money_amount.pack_forget()

    update_balance_in_file(first_name, last_name, pin, current_balance)


def update_balance_in_file(first_name: str, last_name: str, pin: str, new_balance: float) -> None:
    """
    Updates the user's balance in the CSV file.

    Reads the row first
    then replaces the old balance with the new one
    Updates the file by writing the new balance
    """
    rows = []
    with open("data.csv", mode="r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)

    for row in rows:
        if len(row) >= 3 and row[0] == first_name and row[1] == last_name and row[2] == pin:
            row[3] = str(new_balance)

    with open("data.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
def restart(gui:object) -> None:
    '''
    Clears all the buttons and text inputs and brings the user back to the original screen
    '''
    gui.first_name.pack(anchor='w', padx=10, pady=10)
    gui.last_name.pack(anchor='w', padx=10, pady=10)
    gui.pin_number.pack(anchor='w', padx=10, pady=10)
    gui.search_create_button.pack(anchor='w', padx=10, pady=10)

    gui.first_name_input.delete(0, 'end')  # Clear first name input field
    gui.last_name_input.delete(0, 'end')  # Clear last name input field
    gui.pin_number_input.delete(0, 'end')  # Clear pin number input field
    gui.money_amount_input.delete(0, 'end')
    gui.money_decision.set("")

    # Hide elements that should not be shown at the start
    gui.welcome_text.config(text="")  # Clear any welcome text
    gui.to_do_text.config(text="")
    gui.total_amount_text.config(text="")

    gui.money_amount.pack_forget()
    gui.radio_button.pack_forget()
    gui.entry_exit.pack_forget()
    gui.search_create_button.pack()
    gui.pin_number.pack()
    gui.first_name.pack()
    gui.last_name.pack()
def create_click(gui:object, first_name:str, last_name:str, pin:str)->None:
    '''
    Creates a new account with first name last name and pin
    given a balance of 0
    checks if these inputs exists: raises an error
    makes sure that pin is numeric
    '''
    default_balance = 0
    try:
        if not first_name.strip():
            raise ValueError("Enter first name.")
        if not last_name.strip():
            raise ValueError("Enter last name.")
        if not pin.strip():
            raise ValueError("Enter a Pin.")
        if not pin.isdigit():
            raise ValueError("Pin must be numeric.")


    except ValueError as e:
        gui.welcome_text.config(text=str(e), fg="red")
        return  # Exit the function if there's an error

    if not os.path.exists("data.csv"):
        with open("data.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["first_name", "last_name", "pin", "balance"])  # Writing the header

    with open("data.csv", mode="r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 3 and row[0] == first_name and row[1] == last_name and row[2] == pin:
                gui.welcome_text.config(text="Account Exists!", fg="red")
                return  # Exit the function if the account already exists

    # Append the new account to the file
    with open("data.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([first_name, last_name, pin, default_balance])
        gui.welcome_text.config(text="Account Created!", fg="green")