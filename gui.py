#!/usr/bin/python

import Tkinter as tk
import pyperclip
import gnupg


class KeyManagementMenu(tk.Frame):

    """ This part of the application for generating (creating) keys,
        listing keys, deleting keys, and importing and exporting keys.
    """

    def __init__(self, parent=None, menubar=None, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.menubar = menubar
        self.grid(column=0)
        self.create_widgets()

    def create_widgets(self):
        """ Create portions of the key management menu.
        """
        self.parent.config(menu=self.menubar)
        key_mgmt_menu = tk.Menu(self.menubar)  # instantiate menu item
        # add a list of commands to drop down menu
        key_mgmt_menu.add_command(
            label='Generate Key', command=self.generate_key_window)
        key_mgmt_menu.add_command(
            label='Export Key', command=self.export_key_window)
        key_mgmt_menu.add_command(
            label='Scan Key', command=self.scan_key_window)
        # add key management menu option
        self.menubar.add_cascade(label="Key Management", menu=key_mgmt_menu)

    def generate_key_window(self):
        """
        """
        self.top = tk.Toplevel(self.parent)
        self.name_label = tk.Label(
            self.top, text="Name:")
        self.name_label.grid(row=0, sticky='W')
        self.name_entry = tk.Entry(self.top)
        self.name_entry.grid(row=1, column=0)
        self.email_label = tk.Label(
            self.top, text="Email:")
        self.email_label.grid(row=2, sticky='W')
        self.email_entry = tk.Entry(self.top)
        self.email_entry.grid(row=3, column=0)

        # list of possible key sizes
        self.keys_label = tk.Label(
            self.top, text="Key Size:")
        self.keys_label.grid(row=0, column=1)
        key_sizes = ['512', '1024', '2048']
        self.key_size_entry = tk.StringVar(self.top)
        self.key_size_entry.set('Select Key Size')
        self.key_size_list = tk.OptionMenu(
            self.top, self.key_size_entry, *key_sizes)
        self.key_size_list.grid(row=1, column=1)
        # self.key_size_list.insert(tk.END, "entry")

        # select kind of key wanted
        self.key_type_label = tk.Label(
            self.top, text='Key Type:')
        self.key_type_label.grid(row=2, column=1)
        key_types = ['RSA', 'DSA']
        self.key_entry = tk.StringVar(self.top)
        self.key_entry.set('Select Key Type')
        self.key_type_list = tk.OptionMenu(
            self.top, self.key_entry, *key_types)
        self.key_type_list.grid(row=3, column=1)

        self.button = tk.Button(
            self.top, text="Generate key", command=self.cleanup)
        self.button.grid()

        # done

    def export_key_window(self):
        pass

    def scan_key_window(self):
        pass

    def cleanup(self):
        self.value = self.name_entry.get()
        self.top.destroy()
        # done


class EncryptionDecryptionMenu(tk.Frame):

    """
    """

    def __init__(self, parent, menubar):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.menubar = menubar
        self.grid(column=1)
        self.create_widgets()

    def create_widgets(self):

        self.parent.config(menu=self.menubar)
        enc_menu = tk.Menu(self.menubar)
        enc_menu.add_command(
            label='Encrypt Clipboard', command=self.encrypt_clipboard)
        enc_menu.add_command(
            label='Encrypt File', command=self.encrypt_file)
        enc_menu.add_command(
            label='Prompt For Cleartext', command=self.encrypt_prompt)
        self.menubar.add_cascade(label="Encryption", menu=enc_menu)

    def encrypt_clipboard(self):
        cleartext = pyperclip.paste()

    def encrypt_file(self):
        pass

    def encrypt_prompt(self):
        pass


class SigningAndVerificationMenu(tk.Frame):

    def __init__(self, parent=None):

        pass


class HelpMenu(tk.Frame):

    def __init__(self, parent=None, menubar=None, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.menubar = menubar
        self.grid(column=2)
        self.create_widgets()

    def create_widgets(self):
        """ Create portions of the help menu.
        """
        self.parent.config(menu=self.menubar)
        # add a list of commands to drop down menu
        help_menu = tk.Menu(self.menubar)
        help_menu.add_command(
            label='Help with generating a key',
            command=self.generate_keygen_help_window)
        help_menu.add_command(
            label='Help searching for friends keys',
            command=self.generate_search_help_window)
        # add key management menu option
        self.menubar.add_cascade(label="Help", menu=help_menu)

    def generate_keygen_help_window(self):
        self.top = tk.Toplevel(self.parent)
        keygen_help_message = "The first step of encryption is making your own key. This is easy. First, click on the menu labeled 'Key Management' and select 'Generate Key'. You will be asked for your name and email address. Enter this information and click okay. It will take a few minutes for your key to generate. Your computer is having to work really hard! Now you have your key pair! \n \n Note that this will only allow others to send YOU an encrypted message, and only once you send them your public key. If that sounds confusing, select the 'Public vs Private key' in the help menu. Also, in order to encrypt a message for a friend, you need to import your friends public key"
        w = tk.Message(
            master=self.top, text=keygen_help_message, bg="black", fg="white")
        w.pack()

    def generate_search_help_window(self):
        self.top = tk.Toplevel(self.parent)
        search_help_message = "In order to send an encrypted message to a friend, you get your friends public key. The easiest way to do this is to import your friends key from a key server. In order to search a keyserver for your friends key, select the 'Key Management' menu, and then select the 'Scan Key' option. In the window that opens, enter your friends email or name. If their name or email is in the keyserver database, you should be able to select it and press okay. Now you will have your friends key"
        w = tk.Message(
            master=self.top, text=search_help_message, bg="black", fg="white")
        w.pack()

    def help_menu(self):
        pass


class StatusBar(tk.Frame):

    def __init__(self, parent=None):
        pass


# main application subclasses tk.Frame to give
# private namespace for all our callbacks and private functions.


class PrimaryApplication(tk.Frame):

    """ Primary application code.
    """

    def __init__(self, parent=None, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        # QUIT button
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton['fg'] = 'red'
        self.quitButton.grid()

        menubar = tk.Menu(self.parent)
        self.key_menu = KeyManagementMenu(
            parent=self.parent, menubar=menubar)
        self.key_menu.grid(row=0, column=1)
        self.enc_menu = EncryptionDecryptionMenu(
            parent=self.parent, menubar=menubar)
        self.enc_menu.grid(row=0, column=2)
        self.help_menu = HelpMenu(
            parent=self.parent, menubar=menubar)
        self.help_menu.grid(row=0, column=3)


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("550x550+300+300")
    app = PrimaryApplication(parent=root)
    app.master.title('KinderCrypt')
    app.mainloop()
