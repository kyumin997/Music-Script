import logging

try:
    import tkinter as tk

except ImportError:
    import TkInter as tk


class TextHandler(logging.Handler):

    def __init__(self, text):
        logging.Handler.__init__(self)

        self.text = text

    def emit(self, record):
        msg = self.format(record)

        def append():
            self.text.configure(state='normal')
            self.text.insert(tk.END, msg + '\n')
            self.text.configure(state='disabled')

            self.text.yview(tk.END)

        self.text.after(0, append)
