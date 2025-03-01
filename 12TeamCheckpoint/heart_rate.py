# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

import math
import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry


def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("Pendulum Calc")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()


# The controls in a graphical user interface (GUI) are called widgets,
# and each widget is an object. Because a GUI has many widgets and
# each widget is an object, the code to make a GUI usually has many
# variables to store the many objects. Because there are so many
# variable names, programmers often adopt a naming convention to help
# a programmer keep track of all the variables. One popular naming
# convention is to type a three letter prefix in front of the names
# of all variables that store GUI widgets, according to this list:
#
# frm: a frame (window) widget
# lbl: a label widget that displays text for the user to see
# ent: an entry widget where a user will type text or numbers
# btn: a button widget that the user will click


def populate_main_window(frm_main):

    lbl_meters = Label(frm_main, text="In meters")

    ent_pendulum_length = IntEntry(frm_main, width=10, lower_bound=0, upper_bound=1000000000)

    lbl_pendulum_length = Label(frm_main, text="Length of pendulum from earth's gravity, 9.807 m/s^2")

    lbl_calculate = Label(frm_main, width=10)
    lbl_period = Label(frm_main, text="period")

    btn_clear = Button(frm_main, text="Clear")

    lbl_meters.grid(      row=0, column=0, padx=3, pady=3)
    ent_pendulum_length.grid(      row=0, column=1, padx=3, pady=3)
    lbl_pendulum_length.grid(row=0, column=2, padx=0, pady=3)

    lbl_calculate.grid(      row=1, column=2, padx=3, pady=3)
    lbl_period.grid(row=1, column=3, padx=0, pady=3)

    btn_clear.grid(row=2, column=0, padx=3, pady=3, columnspan=4, sticky="w")

    def calculate(event):
        """Compute and display the user's slowest
        and calculateest beneficial heart rates.
        """
        try:
            # Get the user's age.
            length = ent_pendulum_length.get()

            # Compute the user's maximum heart rate.
            period = (2 * math.pi) * math.sqrt((length/9.807))

            # Display the slowest and calculateest benficial
            # heart rates for the user to see.
            lbl_calculate.config(text=f"{period:.5f}")

        except ValueError:
            # When the user deletes all the digits in the age
            # entry box, clear the slowest and calculateest labels.
            lbl_calculate.config(text="")


    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        btn_clear.focus()
        ent_pendulum_length.clear()
        lbl_calculate.config(text="")
        ent_pendulum_length.focus()

    # Bind the calculate function to the age entry box so
    # that the computer will call the calculate function
    # when the user changes the text in the entry box.
    ent_pendulum_length.bind("<KeyRelease>", calculate)

    # Bind the clear function to the clear button so
    # that the computer will call the clear function
    # when the user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the age entry box.
    ent_pendulum_length.focus()


# If this file is executed like this:
# > python heart_rate.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
