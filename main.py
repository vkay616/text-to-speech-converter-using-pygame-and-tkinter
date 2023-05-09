from tkinter import *
import os
from gtts import gTTS
import pygame

def play():
    text = input_field.get("1.0", END)
    output = gTTS(text=text, lang='en', slow=False)
    output.save('output.mp3')
    pygame.mixer.music.load('output.mp3')
    pygame.mixer.music.play(loops=0)


root = Tk()

root.title('TTS')
root.geometry('300x350')
root.configure(background='black')
root.resizable(0, 0)

Label(root, text='Text-to-Speech Application', bg='#000', fg='#fff', font=('helvetica', 12, 'bold'), justify=CENTER).pack(fill=X, pady=5)

input_field = Text(root, height=15)
input_field.pack(fill=X, pady=5)

Button(root, text="LISTEN", command=play, bg="#2d3436", fg="#ffffff", bd=0, font=("helvetica", 10, 'bold')).pack(pady=10)

root.mainloop()
