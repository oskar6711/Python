from pytube import YouTube

from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo


root = Tk()
root.geometry ('400x400')
root.resizable(0, 0)
root.title('Youtube - Downloader')
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

frm = ttk.Frame(root)
frm.grid()

selected_url = StringVar()
result_var = StringVar()


def download_video():
    video = YouTube(selected_url.get())
    stream = video.streams.get_highest_resolution()
    result_var.set('Downloading...')
    stream.download()
    showinfo(
        title='Status',
        message='Downloading Completed!'
    )
    result_var.set('Completed!')
    

url_label = ttk.Label(frm, text="Paste your url here:").grid(column=0, row=0, padx=5, pady=5)
url_entry = ttk.Entry(frm, font = 'arial 15', textvariable=selected_url).grid(column=0, row=1, padx=5, pady=5)
entry_button = ttk.Button(frm, text="Download", command=download_video).grid(column=0, row=2, padx=5, pady=5)
status_entry = ttk.Entry(frm, textvariable=result_var, state='readonly').grid(column=0, row=3, padx=5, pady=5)
quit_button = ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=4, padx=5, pady=5)


root.mainloop()