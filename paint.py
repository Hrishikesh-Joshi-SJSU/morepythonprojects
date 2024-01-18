# ----------------------------------------------------------------------
# Name:        paint
# Purpose:     A very simple coloring application
#
# Author:      Rula Khayrallah
# ----------------------------------------------------------------------
"""
Module to implement a simple coloring app
"""
import tkinter


class PaintApp:

    """
    GUI PaintApp class for a simple coloring application.

    Argument:
    parent (tkinter.Tk): the root window object

    Attributes:
    canvas (tkinter.Canvas): the widget defining the area to be painted
    color (string): the paint color selected - red, green or blue
    """

    # Define a class variable for the default color to be used
    default_color = 'red'

    def __init__(self, parent):
        self.color = self.default_color
        parent.title("CS 122 - Let's Paint!")
        color_frame = tkinter.Frame(parent)
        color_frame.grid()
        green_button = tkinter.Button(color_frame, text='GREEN', width
                                      =5, command=self.green)
        # instantiate our Canvas widget with the root as parent
        green_button.grid(column=0, row=0)
        red_button = tkinter.Button(color_frame, text='RED', width
        =5, command=self.red)
        self.canvas = tkinter.Canvas(parent, width=300, height=300)
        red_button.grid(column=1, row=0)
        blue_button = tkinter.Button(color_frame, text='BLUE', width
        =5, command=self.blue)
        self.canvas = tkinter.Canvas(parent, width=300, height=300)
        blue_button.grid(column=2, row=0)
        # draw a rectangle on the canvas for the background
        self.canvas.create_rectangle(0, 0, 300, 300)
        erase_button = tkinter.Button(parent, text='ERASER', width=30,
                                      command=self.erase)
        erase_button.grid()
        # draw a house
        self.canvas.create_rectangle(175, 150, 275, 250)
        # the roof is a triangle (polygon with 3 sides)
        self.canvas.create_polygon(165, 150, 225, 100, 285, 150,
                                   outline='black', fill='white')
        # draw a flower
        self.canvas.create_oval(50, 200, 75, 225)
        self.canvas.create_oval(50, 175, 75, 200)
        self.canvas.create_oval(50, 225, 75, 250)
        self.canvas.create_oval(25, 187, 50, 212)
        self.canvas.create_oval(25, 212, 50, 237)
        self.canvas.create_oval(75, 187, 100, 212)
        self.canvas.create_oval(75, 212, 100, 237)

        # register our canvas with a geometry manager
        self.canvas.grid()
        self.canvas.bind("<Button-1>", self.paint)
        self.erase()


    def green(self):
        """
        This method is invoked when the GREEN button is clicked.
        It sets the paint color to green.
        """
        self.color = "green"
    def red(self):
        """
        This method is invoked when the RED button is clicked.
        It sets the paint color to red.
        """
        self.color="red"
    def blue(self):
        """
        This method is invoked when the BLUE button is clicked.
        It sets the paint color to blue.
        """
        self.color="blue"
    def erase(self):
        """
        This method is invoked when the ERASE button is clicked.
        It fills all the shapes on the canvas with a white color.
        """
        for shape in self.canvas.find_all():
            self.canvas.itemconfigure(shape, fill='white')

    def paint(self, event):
        """
        This method is invoked when the user clicks on the canvas.
        It fills the enclosing shape with the selected paint color
        :param event: tkinter.Event
        """
        self.canvas.itemconfigure(tkinter.CURRENT, fill=self.color)

def main():
    # create the GUI application main window
    root = tkinter.Tk()
    # Instantiate our painting app object
    painting = PaintApp(root)
    # enter the main event loop and wait for events
    root.mainloop()


if __name__ == '__main__':
    main()
