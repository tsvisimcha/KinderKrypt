#!/usr/bin/python
import Tkinter as tk


class SigningAndVerificationMenu(tk.Frame):

    """ Menu for signing data and verifying public keys.
    """

    def __init__(self, parent=None, menubar=None, gpg=None):
        # intialize the tk frame
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.menubar = menubar
        self.grid(column=2)
        self.create_widgets()

    def create_widgets(self):
        """ Create drop down menu for the Signing and Verification menu.
        """
        return NotImplementedError


if __name__ == '__main__':
    pass
