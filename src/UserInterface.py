import sys
import threading

import logging

from Spek import *

import tkinter as tk

from Handler import TextHandler

from tkinter import Tk, Message, Entry, filedialog, Label, Frame, messagebox, TOP, BOTTOM, X
from tkinter import scrolledtext as ScrolledText


class GUI(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.directory = ""

        self.build_gui()

        self.frame = Frame(parent)
        self.frame.pack()

    def build_gui(self):
        self.root.title("Message Test")
        self.root.option_add('*tearOff', 'FALSE')
        self.grid(column=0, row=0, sticky='ew')
        self.grid_columnconfigure(0, weight=1, uniform='a')
        self.grid_columnconfigure(1, weight=1, uniform='a')
        self.grid_columnconfigure(2, weight=1, uniform='a')
        self.grid_columnconfigure(3, weight=1, uniform='a')
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        st = ScrolledText.ScrolledText(self, state='disabled')
        st.configure(font='TkFixedFont')
        st.grid(column=0, row=1, sticky='w', columnspan=4)

        text_handler = TextHandler(st)

        logging.basiconfig(filename='test.log',
                           level=logging.INFO,
                           format='%(asctime)s - %(levelname)s - %(message)s')

        logger = logging.getLogger()
        logger.addHandler(text_handler)

    def msg_box(self):
        message = Message(self.root, text=self.directory)
        message.config(font=('times', 14), width=500)
        message.pack(side=TOP)

    def get_file_dir(self):
        self.directory = filedialog.askdirectory()

    def hide(self):
        self.root.withdraw()

    def show(self):
        self.root.update()
        self.root.deiconify()
