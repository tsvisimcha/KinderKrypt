#!/usr/bin/python

import Tkinter as tk


class EncryptionDecryptionMenu(tk.Frame):

    """
    """

    def __init__(self, parent=None, menubar=None, gpg=None, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.menubar = menubar
        self.grid(column=1)
        self.create_widgets()

    def create_widgets(self):

        self.parent.config(menu=self.menubar)
        enc_menu = tk.Menu(self.menubar)
        enc_menu.add_command(
            label="Encrypt Message", command=self.encrypt_message)
        enc_menu.add_command(
            label='Encrypt to Clipboard', command=self.encrypt_clipboard)
        enc_menu.add_command(
            label='Encrypt File', command=self.encrypt_file)
        enc_menu.add_command(
            label='Prompt For Cleartext', command=self.encrypt_prompt)
        enc_menu.add_command(
            label="Decrypt Message", command=self.decrypt_message)

        # add to menu
        self.menubar.add_cascade(
            label="Encryption & Decryption", menu=enc_menu)

    def encrypt_message(self):
        """ Encrypt message meant for one or many recipients.
        """
        self.top = tk.Toplevel(self.parent)
        self.recipient_list = self.gpg.get_keys()

    def encrypt_clipboard(self):
        # cleartext = pyperclip.paste()
        pass

    def encrypt_file(self):
        return NotImplementedError

    def encrypt_prompt(self):
        return NotImplementedError

    def decrypt_message(self):
        return NotImplementedError


if __name__ == '__main__':
    pass
