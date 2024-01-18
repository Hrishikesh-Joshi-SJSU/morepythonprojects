# ----------------------------------------------------------------------
# Name:        blinking
# Purpose:     Demonstrate the use of after
#
# Author:      Rula Khayrallah
# ----------------------------------------------------------------------
"""
Module to implement a simple blinking app

The Spartan image appears and disappears
"""
import tkinter


class BlinkApp:

    """
    GUI App class for a blinking Spartan.

    Argument:
    parent (tkinter.Tk): the root window object

    Attributes:
    canvas (tkinter.Canvas): home to the blinking Spartan
    sammy (PhotoImage): Spartan image
    image_id (integer):  ID of the Canvas image object
    """

    # class variables - used as class wide constants
    size = 300  # Canvas side length in pixels
    color = 'yellow'  # Canvas color
    delay = 1000  # blinking delay

    def __init__(self, parent):
        parent.title("CS 122")
        # instantiate our Canvas widget with the root as parent
        self.canvas = tkinter.Canvas(parent, width=self.size,
                                     height=self.size,
                                     background=self.color)
        self.sammy = tkinter.PhotoImage(file='Sammy.gif')
        # image must be saved in the object self.sammy

        self.canvas.grid()
        self.appear()

    def appear(self):
        """
        Add Sammy's image to the center of the canvas
        Call disappear to have the image disappear after a delay
        :return: None
        """
        self.image_id = self.canvas.create_image(self.size / 2,
                                                 self.size / 2,
                                                 image=self.sammy)
        # this puts the image in the center of the canvas
        self.canvas.after(self.delay, self.disappear)
        # makes the appearance temporary

    def disappear(self):
        """
        Remove Sammy's image from the Canvas
        Call appear to have the image reappear after a delay
        :return: None
        """
        self.canvas.delete(self.image_id)
        self.canvas.after(self.delay, self.appear)



def main():
    # create the GUI application main window
    root = tkinter.Tk()
    # instantiate our app object - no need to save it in a variable
    BlinkApp(root)
    # enter the main event loop and wait for events
    root.mainloop()


if __name__ == '__main__':
    main()
