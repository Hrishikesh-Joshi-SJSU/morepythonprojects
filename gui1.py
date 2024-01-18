# ----------------------------------------------------------------------
# Name:        gui1
# Purpose:     Our first tkinter app
#
# Author:      Rula Khayrallah
# ----------------------------------------------------------------------
"""
Module to demonstrate the steps involves in creating a GUI application.
"""
import tkinter  # step 1: import the tkinter module

class GenApp:
    """
    class to support a general purpose GUI application
    """

def main():
    root = tkinter.Tk()  # step 2: create the application main window

    # add your code here
    root.title('CS 122')
    hello = tkinter.Label(root, text='Hello World')
    hello.pack()
    root.mainloop()      # step 5: enter the main event loop and wait
    # root is the top level window(always) for out application. it is an
    # of the class tkinter.Tk
if __name__ == '__main__':
    main()
