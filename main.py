import tkinter
from tkinter import *
from tkinter import Menu
from tkinter import filedialog
import os
from os import path
import pygame
from pygame import *
#from pygame import mixer
#from pygame import mixer.music

pygame.init()

def open():
    global audio_file_name
    audio_file_name = filedialog.askopenfilename(filetypes=(("Audio Files", ".mp3"),   ("All Files", "*.*")))

def play():
    pygame.mixer.music.load(str(audio_file_name))
    pygame.mixer.music.play()



root = Tk()
root.title("Ski3 MP3 player")
root.geometry('700x400')
play_btn = Button(root,text='Play', command=play)
play_btn.grid(column=0,row=2)
menu = Menu(root)
file_item = Menu(menu, tearoff=0)
file_item.add_cascade(label='Открыть',command=open)
menu.add_cascade(label='Файл', menu=file_item)
root.config(menu=menu)
root.mainloop()
