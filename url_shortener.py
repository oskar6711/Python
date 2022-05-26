import pyshorteners

from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

import pyperclip


root = Tk()
root.geometry ('400x400')
root.resizable(0, 0)
root.title('TinyUrl URL-Shortener')
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

frm = ttk.Frame(root)
frm.grid()

selected_url = StringVar()
result_url = StringVar()


def short_url():
    s = pyshorteners.Shortener()
    url = selected_url.get()
    result_url.set(s.tinyurl.short(url))


def copy_result():
    url = result_url.get()
    pyperclip.copy(url)
    showinfo(
        title='',
        message='URL was copied to your clipboard'
    )


url_label = ttk.Label(frm, text="Paste your url here:").grid(column=0, row=0, padx=5, pady=5)
url_entry = ttk.Entry(frm, font = 'arial 15', textvariable=selected_url).grid(column=0, row=1, padx=5, pady=5)
entry_button = ttk.Button(frm, text="Make it shorter", command=short_url).grid(column=0, row=2, padx=5, pady=5)
result_entry = ttk.Entry(frm, text="Result", textvariable=result_url, state='readonly').grid(column=0, row=3, padx=5, pady=5)
copy_button = ttk.Button(frm, text="Copy", command=copy_result).grid(column=2, row=3, padx=5, pady=5)
quit_button = ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=4, padx=5, pady=5)


root.mainloop()