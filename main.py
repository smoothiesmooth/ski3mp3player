import tkinter as tk
from tkinter import Menu
from tkinter import filedialog
import os
from os import path
import pygame


pygame.init()

play_list = list(

)

x = 0

running = True


def open():
    global audio_file_name, label_a
    audio_file_name = filedialog.askopenfilename(filetypes=(
	("MPEG-3 Files", ".mp3"),
	("Microsoft Wave", ".wav"),
	("All Files", "*.*")))
    play_list.append(audio_file_name)
    pygame.mixer.music.load ( play_list.pop() )
    play_list.append(audio_file_name)
    pygame.mixer.music.queue ( play_list.pop() )
    label_a.config(text=audio_file_name)

def play():
    global x, running
    if x==0:
        play_list.append(audio_file_name)
        pygame.mixer.music.load ( play_list.pop() )
        pygame.mixer.music.set_endevent ( pygame.USEREVENT )
        pygame.mixer.music.play()
        while running:
           for event in pygame.event.get():
              if event.type == pygame.USEREVENT:
                 if len ( playlist ) > 0:
                    pygame.mixer.music.queue ( play_list.pop() )
    elif x==1:
        pygame.mixer.music.unpause()
        x = 0


def pause():
    global x
    pygame.mixer.music.pause()
    x = 1

root = tk.Tk()
root.config(bg='grey')
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

pause_btn = tk.Button(
    root,
    text='Pause',
    command=pause,
	bd=0,
	height=2,
	width=10,
	bg='lightgrey',
	fg='white'
)

pause_btn.grid(column=1,row=2)

menu = tk.Menu(root)
file_item = tk.Menu(menu, tearoff=0)
file_item.add_cascade(label='Открыть',command=open)
menu.add_cascade(label='Файл', menu=file_item)
root.config(menu=menu)
label_a = tk.Label(text='', bg="grey", font='consolas')
label_a.grid(column=2,row=3)
root.mainloop()
