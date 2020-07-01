import tkinter as tk
from tkinter import Menu
from tkinter import filedialog
import os
from os import path
import pygame

pygame.init()

def open():
    global audio_file_name, label_a
    audio_file_name = filedialog.askopenfilename(filetypes=(
	("MPEG-3 Files", ".mp3"),
	("Microsoft Wave", ".wav"),
	("All Files", "*.*")))
    label_a.config(text=audio_file_name)

def play():
    pygame.mixer.music.load(str(audio_file_name))
    pygame.mixer.music.play()

root = tk.Tk()
root.config(bg='white')
root.title("Ski3 MP3 player")
root.geometry('700x400')
play_btn = tk.Button(
    root,
    text='Play',
    command=play,
	bd=0,
	height=2,
	width=10,
	bg='lightgrey',
	fg='white'
)
play_btn.grid(column=0,row=2)
menu = tk.Menu(root)
file_item = tk.Menu(menu, tearoff=0)
file_item.add_cascade(label='Открыть',command=open)
menu.add_cascade(label='Файл', menu=file_item)
root.config(menu=menu)
label_a = tk.Label(text='', bg="white", font='consolas')
label_a.grid(column=1,row=2)
root.mainloop()
