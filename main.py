from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from pygame import mixer
import os
root=Tk()
root.title('Music player project by TechVidvan')
root.geometry("920x670+290+85")
root.configure(bg= "#0f1a2b")
root.resizable(False, False)
mixer.init()


def Add_Music():
    path = filedialog.askdirectory ()
    if path:
        os.chdir ( path )
        songs = os.listdire ( path )

        for song in songs:
            if song.endswith ( ".mp3" ):
                playlist.insert ( END, song )


def Play_Music():
    Music_Name = playlist.get ( ACTIVE )
    print ( Music_Name[0:-4] )
    mixer.music.load ( playlist.get ( ACTIVE ) )
    mixer.music.play ()

icon_image = PhotoImage(file="logo.png")
root.iconphoto(False, icon_image)

# Load the logo image
logo_image = PhotoImage(file="logo.png")

logo_label = Label(root, image=logo_image, bg="#0f1a2b")
logo_label.place(x=65, y=115)




def Stop_Music():
    mixer.music.stop()

def Resume_Music():
    mixer.music.unpause()

def Pause_Music():
    mixer.music.pause()


root.title("Music Player")

# Buttons for control
button_play = Button(root, text="Play", font=("times new roman", 12, "bold"), fg="black", bg="light blue", command=Play_Music)
button_play.place(x=135, y=420)

button_stop = Button(root, text="Stop", font=("times new roman", 12, "bold"), fg="black", bg="light blue", command=Stop_Music)
button_stop.place(x=60, y=500)

button_resume = Button(root, text="Resume", font=("times new roman", 12, "bold"), fg="black", bg="light blue", command=Resume_Music)
button_resume.place(x=115, y=500)

button_pause = Button(root, text="Pause", font=("times new roman", 12, "bold"), fg="black", bg="light blue", command=Pause_Music)
button_pause.place(x=200, y=500)

# Music playlist
frame_music = Frame(root, bd=2, relief=RIDGE)
frame_music.place(x=330, y=350, width=560, height=250)

button_add_music = Button(root, text="Add Music", width=15, height=2, font=("times new roman", 12, "bold"), fg="black", bg="#21b3de", command=Add_Music)
button_add_music.place(x=330, y=300)

scroll = Scrollbar(frame_music)
playlist = Listbox(frame_music, width=100, font=("Times new roman", 10), bg="black", fg="grey", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=LEFT, fill=BOTH)
playlist.insert(END,"Ed_Sheeran_-_Perfect.mp3")

root.mainloop ()