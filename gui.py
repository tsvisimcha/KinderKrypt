#!/usr/bin/python

import Tkinter as tk


class KeyManagementMenu(tk.Frame):

    """ This part of the application for generating (creating) keys,
        listing keys, deleting keys, and importing and exporting keys.
    """

    def __init__(self, parent=None, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        
        menubar = tk.Menu(self.parent)
        self.parent.config(menu=menubar)

        key_mgmt_menu = tk.Menu(menubar)

        key_mgmt_menu.add_command(
            label='Generate Secret Key', command=lambda: "666")
        menubar.add_cascade(label="Key Management", menu=key_mgmt_menu)
        # self.key_mangagement_menu = KeyManagementMenu()

    def generate_key():
        """
        """

        return NotImplementedError


class EncryptionDecrytionMenu(tk.Frame):

    def __init__(self, parent=None):

        pass


class SigningAndVerificationMenu(tk.Frame):

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
        self.parent = parent
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        # QUIT button
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton['fg'] = 'red'
        # self.quitButton.pack({'side': 'left'})
        self.quitButton.grid()

        self.key_menu = KeyManagementMenu(parent=self.parent)


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("550x550+300+300")
    app = PrimaryApplication(parent=root)
    app.master.title('KinderCrypt')
    app.mainloop()
