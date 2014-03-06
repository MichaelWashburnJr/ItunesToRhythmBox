#!/usr/bin/env python3

"""
file: main.py
Program: Playlist Converter
Author: Michael Washburn
"""

from tkinter import *
from tkinter.filedialog import *
import subprocess


### CONVERTER ###
def process_all(file, Directory):
    """
    This function takes the itunes playlist and returns
    all the information needed to write to our new .pls
    """
    songs = ""
    n=1
    for line in file:
        line = line.split('\t')
        if line[0] != 'Name':
            path = line[len(line)-1]
            path = path.split("\\")
            ext = path[-1]
            ext = ext.rstrip('\n') 
            name = line[0] 
            Title = "Title" + str(n) + "=" + str(name)
            Location = "File" + str(n) + "=" + "file://" + Directory + '/' + str(ext)
            Location = Location.split()
            newLocation = ""
            for part in Location:
                newLocation = newLocation + str(part) + "%20"
            newLocation = newLocation[:-3]
            n +=1
            songs = songs + newLocation + '\n' + Title + '\n'
    return songs, n-1


def main_all():
    """
    This function is called when our start button is pressed and initializes
    our new file, then calls process to get the necessary parts from the
    itunes playlist, then builds the new file.
    """
    global in1
    global in2
    global in4
    iplaylist = in1
    new = in2
    new.write('[playlist] \n')
    name = input3.get()
    new.write('X-GNOME-Title=' + name + '\n')
    
    Directory = in4
    songs, n = process_all(iplaylist, Directory)
    new.write('NumberOfEntries=' + str(n) + '\n')
    new.write(songs)
    output.configure(text='Finished')

### GUI Functions ###
  
def saveFile():
    """ sets variables as they are entered """
    global in1
    global in2
    global in3
    global in4
    if not in1:
        in1 = askopenfilename()
        in1 = open(in1)
    elif in2 == "":
        in2 = asksaveasfile(mode='w')
    elif in4 == "":
        in4 = askdirectory()
        
def Help():
    """Opens the help.txt when the help button is pressed"""
    subprocess.call(["xdg-open",'help.txt'])

        
    
def Reset():
    """Resets the variables """
    in1 = ""
    in2 = ""
    in4 = ""  
    

### GUI ###            
root = Tk()
root.wm_title("Playlist Converter")

in1 = ""
in2 = ""
in4 = "" 

prompt1 = Label(root,text="Enter the whole directory of your itunes playlist including the name.txt: ")
input1 = Button(root, text='Select your iTunes Playlist', command=saveFile)
prompt2 = Label(root,text="Enter the entire directory of where the new playlist should be saved: ")
input2 = Button(root, text='Save as..', command=saveFile)
prompt3 = Label(root,text="Enter the name of the new playlist here: ")
input3 = Entry(root)
input3.insert(0,"New Playlist")
prompt4 = Label(root,text="Enter the directory of the folder containing your songs: ")
input4 = Button(root, text='Locate Directory', command=saveFile)

output = Label(root,text="When this text reads 'Finished', your playlist was converted.")

prompt1.grid(sticky=E)
input1.grid(row=0,column=1)
prompt2.grid(sticky=E)
input2.grid(row=1,column=1)
prompt3.grid(sticky=E)
input3.grid(row=2,column=1)
prompt4.grid(sticky=E)
input4.grid(row=3,column=1)

output.grid(row=5,column=0)


input3.focus()

button = Button(root,text="Start",command=main_all)

button.grid(row=5,column=1,sticky=W)

reset = Button(root,text="Reset",command=Reset)

reset.grid(row=5,column=1)

helpB = Button(root,text="Help",command=Help)

helpB.grid(row=5,column=1,sticky=E)
   
root.mainloop()
