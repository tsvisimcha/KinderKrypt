#!/usr/bin/python
import Tkinter as tk
import ttk
import pyperclip
import gnupg


class KeyManagementMenu(tk.Frame):

    """ This part of the application for generating (creating) keys,
        listing keys, deleting keys, and importing and exporting keys.
    """

    def __init__(self, parent=None, menubar=None, gpg=None, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        self.gpg = gpg
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
        key_mgmt_menu.add_command(
            label='Search for keys', command=self.search_keys)
        key_mgmt_menu.add_command(
            label='Upload key', command=self.upload_key)
        # add key management menu option
        self.menubar.add_cascade(label="Key Management", menu=key_mgmt_menu)

    def generate_key_window(self):
        """ Pops up window for key generation.
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
        self.key_type_entry = tk.StringVar(self.top)
        self.key_type_entry.set('Select Key Type')
        self.key_type_list = tk.OptionMenu(
            self.top, self.key_type_entry, *key_types)
        self.key_type_list.grid(row=3, column=1)

        self.button = tk.Button(
            self.top, text="Generate key", command=self.generate_key)
        self.button.grid()

        # done

    def search_keys(self):
        self.top = tk.Toplevel(self.parent)
        self.search_label = tk.Label(
            self.top, text="Enter emails or names:")
        self.search_label.grid(row=0, sticky='W')
        self.search_entry = tk.Entry(self.top)
        self.search_entry.grid(row=1, column=0)
        self.button = tk.Button(
            self.top, text="Search",
            command=self.key_search)
        self.button.grid()

    def upload_key(self):

        pass

    def export_key_window(self):
        pass

    def scan_key_window(self):
        pass

    def generate_key(self):
        # since all these params are attached to self..
        params = {'key_type': self.key_type_entry.get(),
                  'key_length': self.key_size_entry.get(),
                  'name_real': self.name_entry.get(),
                  'name_email': self.email_entry.get()}
        print params
        key = self.gpg.gen_key_input(**params)
        print key
        self.top.destroy()
        return key

    def key_search(self):
        search_str = self.search_entry.get()
        return NotImplementedError

    def cleanup(self):
        self.value = self.name_entry.get()
        self.top.destroy()
        # done


class EncryptionDecryptionMenu(tk.Frame):

    """
    """

    def __init__(self, parent=None, menubar=None, gpg=None):
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
        # cleartext = pyperclip.paste()
        pass

    def encrypt_file(self):
        pass

    def encrypt_prompt(self):
        pass


class KeyListBox(tk.Frame):

    """ Displays list of keys within a ListBox in the main application.
    """

    def __init__(self, parent=None, gpg=None):
        tk.Frame.__init__(self, parent)
        self.gpg = gpg
        self.parent = parent
        self.key_list_box = ttk.Treeview(
            master=self.parent, columns=('Email', 'Public Key'),
            show='headings')
        for col in ('Email', 'Public Key'):
            self.key_list_box.heading(col,
                                      text=col.title(),
                                      command=lambda c=col: sorted(self.key_list_box, key=c))
        for key in gpg.list_keys():
            pass
        # for key in gpg.list_keys():
        #     self.key_list_box.insert(tk.END, key)
        self.key_list_box.grid(row=5)


class SigningAndVerificationMenu(tk.Frame):

    """ Menu for signing data and verifying public keys.
    """

    def __init__(self, parent=None, menubar=None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.menubar = menubar
        self.grid(column=2)
        self.create_widgets()

    def create_widgets(self):
        # sig_ver_menu = tk.Menu(self.menubar)
        pass


class HelpMenu(tk.Frame):

    def __init__(self, parent=None, menubar=None, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.menubar = menubar
        self.grid(column=3)
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
        # Help understanding public key encryption
        help_menu.add_command(
            label='How does public key encryption work?',
            command=self.generate_gpg_info_window)
        # Nazi help
        help_menu.add_command(
            label='What if Nazis steal my private key?',
            command=self.nazi_query)
        # add key management menu option
        self.menubar.add_cascade(label="Help", menu=help_menu)

    def generate_keygen_help_window(self):
        self.top = tk.Toplevel(self.parent)
        keygen_help_message = "The first step of encryption is "  \
            "making your own key. This is easy. First, click on the " \
            "menu labeled 'Key Management' and select 'Generate Key' "  \
            "You will be asked for your name and email address." \
            "Enter this information and click okay. It will take " \
            "a few minutes for your key to generate. Your computer "\
            "is having to work really hard! Now you have your key"\
            "pair! \n \n Note that this will only allow others to "\
            "send YOU an encrypted message, and only once you "\
            "send them your public key. If that sounds confusing, "\
            "select the 'Public vs Private key' in the help menu. "\
            "Also, in order to encrypt a message " \
            "for a friend, you need to import your friends public key"
        w = tk.Message(
            master=self.top, text=keygen_help_message,
            bg="black", fg="white", font=("Arial", 12, "bold"))
        w.pack()

    def generate_search_help_window(self):
        self.top = tk.Toplevel(self.parent)
        search_help_message = "In order to send an encrypted "\
            "message to a friend, you get your friends public key. "\
            "The easiest way to do this is to import your friends key " \
            "from a key server. In order to search a keyserver for " \
            "your friends key, select the 'Key Management' menu, and "\
            "then select the 'Scan Key' option. In the window that "\
            "opens, enter your friends email or name. If their name "\
            "or email is in the keyserver database, you should be able "\
            "to select it and press okay. Now you will have your friends key"
        w = tk.Message(
            master=self.top, text=search_help_message, bg="black",
            fg="white", font=("Arial", 12, "bold"))
        w.pack()

    def generate_gpg_info_window(self):
        self.top = tk.Toplevel(self.parent)
        gpg_info_message = "What is public key encryption? \n \n "\
            "Public key encryption is a way to send encrypted messages "\
            "without ever having to exchange messages in person. It is "\
            "as if I created a lock with only one key, and then copied "\
            "that lock and gave it to all of my friends and acquaintances. "\
            "Then anyone with my lock could put a message in a box, lock "\
            "it with the special lock, and send it to me. Since I made all "\
            "the locks, and only I have the key, the message is secure. \n \n "\
            "Of course, these are not actual locks, but complex mathematical "\
            "locks stored in the computer. When you generate a key in Kinder"\
            "Kyrpt, you are really making two keys. A public key and a private "\
            "key. The public key is like the open lock. You can pass it out to "\
            "any of your friends and acquaintances, or upload it to a keyserver "\
            "that anyone can access. That way anyone can send you a message that "\
            "only you can read. This works because only you have your private key."
        w = tk.Message(
            master=self.top, text=gpg_info_message, bg="black",
            fg="white", font=("Arial", 12, "bold"))
        w.pack()
        # Because it is... if you think about it
        everything = "fine"

    def nazi_query(self):
        self.top = tk.Toplevel(self.parent)
        nazi_message = "Then you are totally fucked."
        w = tk.Message(
            master=self.top, text=nazi_message, bg="black",
            fg="white", width=400, font=("Arial", 15, "bold"))
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
        # TODO: general home directory string? across os's.
        self.gpg = gnupg.GPG(gnupghome='test')
        self.parent = parent
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        # QUIT button
        self.quitButton = tk.Button(
            self.parent, text='Quit', command=self.quit)
        self.quitButton['fg'] = 'red'
        self.quitButton.grid(row=1, column=0)

        menubar = tk.Menu(self.parent)

        # key management menu
        self.key_menu = KeyManagementMenu(
            parent=self.parent, menubar=menubar, gpg=self.gpg)
        self.key_menu.grid(row=0, column=1)

        # encryption and decrytion menu
        self.enc_menu = EncryptionDecryptionMenu(
            parent=self.parent, menubar=menubar, gpg=self.gpg)
        self.enc_menu.grid(row=0, column=2)

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
    root.geometry("400x350+300+300")
    app = PrimaryApplication(parent=root)
    app.master.title('KinderKrypt')
    app.mainloop()
