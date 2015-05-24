#!/usr/bin/python
import Tkinter as tk


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
