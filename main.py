from os import system
from time import sleep
import tkinter as tk
from threading import Thread
from tkinter import *

#tkinter blurry on windows fix
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

default = '#3E3D53'

def main():
    root = tk.Tk()
    root.geometry('600x200')
    root.title('Audiotube')
    root.resizable(False, False)
    
    #cosmetics
    tk.Canvas(root, highlightthickness=0, bg=default, height=400, width=600).place(x=0, y=0)

    #textvariables    
    pname = tk.StringVar()
    link = tk.StringVar()

    #Entry Boxes
    tk.Label(root, text='Nazwa playlisty:', foreground='white', font='Consolas 14', bg=default).place(x=7, y=18)
    pnamebox = tk.Entry(root, textvariable=pname, background='#d3d3d3', width=30, font='Consolas 14', highlightbackground='#27263a')
    pnamebox.place(x=10, y=50)
    tk.Label(root, text='Link:', foreground='white', font='Consolas 14', bg=default).place(x=7, y=98)
    linkbox = tk.Entry(root, textvariable=link, background='#d3d3d3', width=30, font='Consolas 14', highlightbackground='#27263a')
    linkbox.place(x=10, y=130)
    
    def download():
        pnametemp = pnamebox.get()
        linktemp = linkbox.get()
        linkbox.delete(0, END)
        linkbox.insert(0, "")
        pnamebox.delete(0, END)
        pnamebox.insert(0, "")
        system('mkdir Music\\' + pnametemp)
        system('yt-dlp.exe -P Music\\' + pnametemp + ' ' + '-x --audio-format mp3 --embed-thumbnail ' + linktemp)

    def dwstart():
        dupa = Thread(target = download)
        dupa.start()

    tk.Button(root, text='Pobierz', font='Consolas 20', background='#1e1d2d', foreground='white', activebackground='#1e1d2d', activeforeground='white', relief='raised', command=dwstart).place(x=430, y=70)
    root.mainloop()

mainth = Thread(target = main)
mainth.start()
mainth.join()
