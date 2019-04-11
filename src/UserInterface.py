import sys
import threading

from Spek import *
from tkinter import Tk, Message, Entry, filedialog


class MusicUI:

    def __init__(self, parent):
        self.root = parent
        self.root.title = "Message Test"
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.directory = ""

    def msg_box(self):
        msg = Message(self.root, text='Path: ' + self.directory)
        msg.config(font=('times', 12))
        msg.pack()

    def get_file_dir(self):
        self.directory = filedialog.askdirectory()

    def hide(self):
        self.root.withdraw

    def show(self):
        self.root.update()
        self.root.deiconify()
