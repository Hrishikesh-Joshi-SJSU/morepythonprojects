import tkinter  # step 1: import the tkinter module

class GenApp:
    """
    class to support a general purpose GUI application
    """
    def __init__(self, parent):
        parent.title('CS 122')
        start_button = tkinter.Button(parent, text='START', width=20,
                                      command=self.start)
        start_button.grid()
        stop_button = tkinter.Button(parent, text='STOP', width=20,
                                     command=self.stop)
        stop_button.grid()

        self.status = tkinter.Label(parent, text='Ready to start')
        self.status.grid()
    def start(self):
        self.status.configure(text='In progress', foreground='green')
    def stop(self):
        self.status.configure(text='All done', foreground='red')
def main():
    root = tkinter.Tk()  # step 2: create the application main window
    gen_app = GenApp(root)
    # add your code here
    root.title('CS 122')
    hello = tkinter.Label(root, text='Hello World')
    hello.pack()
    root.mainloop()      # step 5: enter the main event loop and wait
    # root is the top level window(always) for out application. it is an
    # of the class tkinter.Tk
if __name__ == '__main__':
    main()