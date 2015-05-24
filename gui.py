#!/usr/bin/python

import Tkinter as tk


class KeyManagementMenu(tk.Frame):

    """ This part of the application for generating (creating) keys,
        listing keys, deleting keys, and importing and exporting keys.
    """

    def __init__(self, parent=None, *args, **kwargs):
        tk.Frame.__init__(self, parent, )
        self.parent = parent
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create portions of the key management menu.
        """
        menubar = tk.Menu(self.parent)
        self.parent.config(menu=menubar)
        key_mgmt_menu = tk.Menu(menubar)  # instantiate menu item
        # add a list of commands to drop down menu
        key_mgmt_menu.add_command(
            label='Generate Key', command=self.generate_key_window)
        key_mgmt_menu.add_command(
            label='Export Key', command=self.export_key_window)
        key_mgmt_menu.add_command(
            label='Scan Key', command=self.scan_key_window)

        menubar.add_cascade(label="Key Management", menu=key_mgmt_menu)

    def generate_key_window(self):
        """
        """
        self.top = tk.Toplevel(self.parent)
        self.label = tk.Label(self.top, text="Generate Key")
        self.label.pack()
        self.name_entry = tk.Entry(self.top)
        self.name_entry.pack()

        self.key_size_list = tk.Listbox(self.parent)
        self.key_size_list.insert(tk.END, "entry")
        self.key_size_list.pack()

        self.button = tk.Button(
            self.top, text="Generate", command=self.cleanup)
        self.button.pack()
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

    def __init__(self, parent=None):

        pass


class SigningAndVerificationMenu(tk.Frame):

    def __init__(self, parent=None):

        pass


class HelpMenu(tk.Frame):

    def __init__(self, parent=None):
        pass

    def generate_help_window(self):
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

        self.key_menu = KeyManagementMenu(parent=self.parent)
        self.help_menu = HelpMenu(parent=self.parent)


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("550x550+300+300")
    app = PrimaryApplication(parent=root)
    app.master.title('KinderCrypt')
    app.mainloop()
