from gui import *
from tkinter import *

def main():
    '''
    Sets up the main window and where you would run the code
    '''
    window = Tk()
    window.title('ATM')
    window.geometry('480x440')
    window.resizable(width=False, height=False)  # Disables window resizing
    Gui(window)
    window.mainloop()

if __name__ == "__main__":
    main()