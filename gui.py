#!/usr/bin/python

import Tkinter as tk


class NavBar(tk.Frame):

    def __init__(self, parent=None):
        pass


class StatusBar(tk.Frame):

    def __init__(self, parent=None):
        pass


class Main(tk.Frame):
    pass
# main application subclasses tk.Frame to give
# private namespace for all our callbacks and private functions.


class PrimaryApplication(tk.Frame):

    def __init__(self, parent=None, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.grid()
        self.createWidgets()
        # self.statusbar = StatusBar()
        # self.navigation = NavBar()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton['fg'] = 'red'
        # self.quitButton.pack({'side': 'left'})
        self.quitButton.grid()

    # TODO: create buttons for generating a PGP key


if __name__ == '__main__':

    app = PrimaryApplication()
    app.master.title('KinderCrypt')
    app.mainloop()
