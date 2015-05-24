#!/usr/bin/python
from PIL import Image, ImageTk
import Tkinter as tk
# import tkFileDialog
import gnupg

# import all the menus that are part of our application
from encryption_decryption import EncryptionDecryptionMenu
from sign_verify import SigningAndVerificationMenu
from key_management import KeyManagementMenu
from help_menu import HelpMenu


class KeyListBox(tk.Frame):

    """ Displays list of available keys within a ListBox in the main application.
    """

    def __init__(self, parent=None, gpg=None):
        tk.Frame.__init__(self, parent)
        self.gpg = gpg
        self.parent = parent
        self.vertical_scroll_bar = tk.Scrollbar(
            orient="vertical", command=self.on_vsb)
        # synchronize two list boxes with one scroll bar
        self.box_one = tk.Listbox(
            self.parent, yscrollcommand=self.vertical_scroll_bar.set)
        self.box_two = tk.Listbox(
            self.parent, yscrollcommand=self.vertical_scroll_bar.set)
        self.vertical_scroll_bar.grid(row=1, column=4)
        self.box_one.grid(row=1, column=2)
        self.box_two.grid(row=1, column=3)
        for key in self.gpg.list_keys():
            self.box_one.insert('end', key['uids'][0])
            self.box_two.insert('end', key['fingerprint'])

    def on_vsb(self, *args):
        """ Vertical Scrolling event
        """
        self.box_one.yview(*args)
        self.box_two.yview(*args)

    def on_mouse_wheel(self, event):
        self.box_one.yview("scroll", event.delta, "units")
        self.box_two.yview("scroll", event.delta, "units")
        # prevents defaults bindings from firing, which could
        # possibly scroll twice over.
        return "break"


class StatusBar(tk.Frame):

    """ Gives current status of whatever process is running within KinderKrypt.
    """

    def __init__(self, parent=None):
        pass


# main application subclasses tk.Frame to give
# private namespace for all our callbacks and private functions.


class KinderKrypt(tk.Frame):

    """ Primary application code.
    """

    def __init__(self, parent=None, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        # TODO: general home directory string? across os's.
        self.gpg = gnupg.GPG(gnupghome='test')
        self.parent = parent
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.img = ImageTk.PhotoImage(Image.open('dead_mac.png'))
        self.img_label = tk.Label(self.parent, image=self.img).grid(row=1)
        # QUIT button
        self.quitButton = tk.Button(
            self.parent, text='Quit', command=self.quit)
        self.quitButton['fg'] = 'red'
        self.quitButton.grid(row=2, column=0)

        menubar = tk.Menu(self.parent)

        # key management menu
        self.key_menu = KeyManagementMenu(
            parent=self.parent, menubar=menubar, gpg=self.gpg)
        self.key_menu.grid(row=0, column=1)

        # encryption and decrytion menu
        self.enc_menu = EncryptionDecryptionMenu(
            parent=self.parent, menubar=menubar, gpg=self.gpg)
        self.enc_menu.grid(row=0, column=2)

        # signing and verification menu
        self.veri_menu = SigningAndVerificationMenu(
            parent=self.parent, menubar=menubar, gpg=self.gpg)
        self.veri_menu.grid(row=0, column=3)

        # informational help menu
        self.help_menu = HelpMenu(
            parent=self.parent, menubar=menubar)
        self.help_menu.grid(row=0, column=4)

        # instantiate key list box
        self.key_list_box = KeyListBox(
            parent=self.parent, gpg=self.gpg)
        self.key_list_box.grid(row=2, column=0)


if __name__ == '__main__':
    # begin application.
    root = tk.Tk()
    root.geometry("420x200+300+300")
    app = KinderKrypt(parent=root)
    app.master.title('KinderKrypt')
    app.mainloop()
