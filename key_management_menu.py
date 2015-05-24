#!/usr/bin/python
import Tkinter as tk


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
        key_sizes = ['1024', '2048']
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
        self.search_button = tk.Button(
            self.top, text="Search",
            command=self.key_search)
        self.save_button = tk.Button(self.top,
                                     text="Save selected key",
                                     command=self.save_key)
        self.save_button.grid(row=5, column=0)
        self.search_button.grid(row=3, column=0)
        self.output_box = tk.Listbox(master=self.top, width=100)
        self.output_box.grid(row=4, column=1)

    def upload_key(self):
        """ Upload key to keyserver.
        """
        self.top = tk.Toplevel(self.parent)
        keyserver_list = ['esperanza.ubuntu.com',
                          'gozer.rediris.es',
                          'kerckhoffs.surfnet.nl',
                          'keys.kfwebs.net',
                          'keys.niif.hu',
                          'keyserver.stack.nl',
                          'lorien.prato.linux.it',
                          'pgp.zdv.uni-mainz.de',
                          'stinkfoot.org']
        # self.key_list = self.gpg.list_keys()
        # self.server_list = tk.OptionMenu(
        #     self.top, self.)
        print keyserver_list

    def export_key_window(self):
        """ Export keys.
        """
        pass

    def scan_key_window(self):
        """ Opens a file and scans for keys without importing them to local keyring.
        """
        self.text = tk.Text()
        file_types = [('Text files', '*.txt'), ('All files', '*')]
        dialogue = tkFileDialog.Open(self, filetypes=file_types)
        f = dialogue.show()
        if f != '':
            # gpg --with-fingerprint --with-colons filename
            results = gnupg.scans(f)
            self.text.insert(tk.END, results)

    def generate_key(self):
        # since all these params are attached to self..
        params = {'key_type': self.key_type_entry.get(),
                  'key_length': self.key_size_entry.get(),
                  'name_real': self.name_entry.get(),
                  'name_email': self.email_entry.get()}
        print params
        key_inputs = self.gpg.gen_key_input(**params)
        self.top.config(cursor="wait")
        print "Generating secret key..."
        key = self.gpg.gen_key(key_inputs)
        self.top.config(cursor="")
        self.top.destroy()
        return key

    def key_search(self):
        search_str = self.search_entry.get()
        result_str = self.gpg.search_keys(search_str)
        if result_str == []:
            result_str = "No matches were found"
        self.output_box.insert(tk.END, result_str)

    def save_key(self):
        key_data = self.output_box.get(tk.ACTIVE)
        if key_data != []:
            import_result = self.gpg.import_keys(key_data)
            print import_result

    def cleanup(self):
        self.value = self.name_entry.get()
        self.top.destroy()
        # done
