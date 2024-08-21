from tkinter import * 
from PIL import Image,ImageTk,ImageSequence 
import time
import pygame 
from pygame import mixer
mixer.init()

root = Tk()
root.geometry("1920x1080")

def play_gif():
    root.lift()
    root.attributes("-topmost",True)
    global img
    img = Image.open("iron men.gif")
    lbl = Label(root)
    lbl.place(x=250,y=170)
    i=0
    mixer.music.load("ironmenmusic 3.mp3")
    mixer.music.play()
    
    for img in ImageSequence.Iterator(img):
        img = img.resize((1000,500))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        time.sleep(0.05)
    root.destroy()

play_gif()
root.mainloop()