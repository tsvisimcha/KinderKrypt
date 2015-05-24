#!/usr/bin/python
import Tkinter as tk


class SigningAndVerificationMenu(tk.Frame):

    """ Menu for signing data and verifying public keys.
    """

    def __init__(self, parent=None, menubar=None, gpg=None):
        # intialize the tk frame
        tk.Frame.__init__(self, parent)
        self.gpg = gpg
        self.parent = parent
        self.menubar = menubar
        self.grid(column=5)
        self.create_widgets()

    def create_widgets(self):
        """ Create drop down menu for the Signing and Verification menu.
        """
        self.parent.config(menu=self.menubar)
        sign_verify_menu = tk.Menu(self.menubar)
        sign_verify_menu.add_command(
            label="Sign with Private Key", command=self.sign)
        sign_verify_menu.add_command(
            label="Verify data recieved", command=self.verify)
        self.menubar.add_cascade(
            label="Signing & Verification", menu=sign_verify_menu)

    def sign(self):
        return NotImplementedError

    def verify(self):
        return NotImplementedError

if __name__ == '__main__':
    pass
