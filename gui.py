#!/usr/bin/python

import Tkinter as tk


class KeyManagementBar(tk.Frame):

    def __init__(self, parent=None):
        self.grid()
        self.create_widgets
        pass

    def create_widgets(self):
        self.generate_key_button = tk.Button(self,
                                             text="Generate Secret Key",
                                             command=self.generate_key)

    def generate_key():
        """ Generate key pairs.
        """

        return NotImplementedError


class EncryptionDecrytionBar(tk.Frame):

    def __init__(self, parent=None):

        pass


class SigningAndVerificationBar(tk.Frame):

    def __init__(self, parent=None):

        pass


class StatusBar(tk.Frame):

    def __init__(self, parent=None):
        pass


# main application subclasses tk.Frame to give
# private namespace for all our callbacks and private functions.


class PrimaryApplication(tk.Frame):

    def __init__(self, parent=None, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.grid()
        self.create_widgets()
        # self.statusbar = StatusBar()
        # self.navigation = NavBar()

    def create_widgets(self):
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton['fg'] = 'red'
        # self.quitButton.pack({'side': 'left'})
        self.quitButton.grid()

    # TODO: create buttons for generating a PGP key


if __name__ == '__main__':

    app = PrimaryApplication()
    app.master.title('KinderCrypt')
    app.mainloop()
