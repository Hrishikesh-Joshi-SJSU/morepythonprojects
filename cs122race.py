# ----------------------------------------------------------------------
# Name:        cs122race
# Purpose:     demonstrate the use of tags
#
# Author:      Rula Khayrallah
# ----------------------------------------------------------------------
"""
Demonstrate the use of Canvas tags.

The user clicks on one or more shapes to select them.
When the GO button is pressed, the selected shapes move to the right.
"""
import tkinter


class TagDemo:

    """
    class to demonstrate the use of tags.

    Argument:
    parent: (tkinter.Tk) the root window object

    Attribute:
    canvas: (tkinter.Canvas) A Canvas widget
    """

    def __init__(self, parent):
        parent.title('CS 122')
        # create a GO button and associate it with the go method
        start_button = tkinter.Button(parent, text='GO', width=20,
                                      command=self.go)
        start_button.grid() # register it with a geometry manager

        # create a Canvas widget
        self.canvas = tkinter.Canvas(parent, width=500, height=200,
                                     background='lawn green')
        # Create some shapes
        for count in range(10, 180, 20 ):
            self.canvas.create_oval(10, 10+count,
                                    20, 20+count,
                                    fill='red',
                                    tags='car')
        # bind a click on the Canvas to the select method.
        # each oval has a tag 'car'.
        self.canvas.bind("<Button-1>", self.select)
        self.canvas.grid()

    def select(self, event):
        """
        Toggle the color and the tag of the clicked circle
        :param event (tkinter.Event)
        :return: None
        """
        # toggle the color between red and blue
        if self.canvas.itemcget(tkinter.CURRENT, 'fill') == 'red':
            self.canvas.itemconfigure(tkinter.CURRENT, fill='blue')
        else:
            self.canvas.itemconfigure(tkinter.CURRENT, fill='red')
        # update the tag
        current_tags = self.canvas.gettags(tkinter.CURRENT)
        if 'selected' in current_tags:
            self.canvas.dtag(tkinter.CURRENT,'selected')
        else:
            self.canvas.addtag_withtag( 'selected', tkinter.CURRENT)

    def go(self):
        """
        Move all circles that have been tagged "selected" 10
        pixels to the right.
        :return:
        """
        self.canvas.move('selected', 10, 0)


def main():
    root = tkinter.Tk() # create the GUI application main window
    TagDemo(root)       # instantiate our app object
    root.mainloop()     # enter the main event loop and wait


if __name__ == '__main__':
    main()
