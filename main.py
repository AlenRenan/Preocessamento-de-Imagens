from tkinter import *  # Import from GUI api
from tkinter import ttk     # Import from GUI api
import logic    # logic.py

"""
Main Class
"""


class Application:
    """
    Window Configs
    """
    root = Tk()  # Constructor
    root.geometry("300x600")  # Window Size
    root.configure(background='#B2D5F0')
    root.resizable(False, False)  # Impossible to resize the window
    root.title("Select an Option")  # Window Title

    """
    histogram Button Configs
    """
    histogram_button = ttk.Button(
        root,
        text='Histogram',
        command=logic.histogram_logic
    )

    histogram_button.pack(
        ipadx=50,
        ipady=50,
        expand=True
    )
    """
       binaryGrey Button Configs
    """
    binaryGrey_button = ttk.Button(
        root,
        text='Black and White',
        command=logic.binary_logic
    )
    binaryGrey_button.pack(
        ipadx=40,
        ipady=50,
        expand=True
    )
    """
        filters Button Configs
    """
    filters_button = ttk.Button(
        root,
        text='Add filters',
        command=logic.filters_logic
    )
    filters_button.pack(
        ipadx=50,
        ipady=50,
        expand=True
    )
    """
        exit Button Configs
    """
    exit_button = ttk.Button(
        root,
        text='Exit',
        command=root.destroy

    )
    exit_button.pack(
        ipadx=10,
        ipady=10,
        expand=True
    )
    root.mainloop()
