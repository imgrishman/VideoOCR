#from lib2to3.pgen2 import driver
import tkinter
import fileinput
from tkinter import *
import Video
import time
#import STT



# import filedialog module
from tkinter import filedialog
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("all files","*.mp4*"),("all files",   "*.*")))
    #Video.getFrame(filename , 0)
    # Change label contents
    
    #STT.extract()
    label_file_explorer.configure(text="Video Executing: "+filename)
    Video.getFrame(filename ,0)
    label_file_explorer.configure(text="Video Executing completed ")
    
    #STT.extract(filename)
      
                                                                                                  
# Create the root window
window = Tk()
  
# Set window title
window.title('OCR')
  
# Set window size
window.geometry("370x310")
  
#Set window background color
window.config(background = "white")
  
# Create a File Explorer label
label_file_explorer = Label(window,
                            text = "Please select the video file",
                            width = 50, height = 3,
                            fg = "blue")
  
      
button_explore = Button(window,
                        text = "Browse Files",
                        command = browseFiles)
  
button_exit = Button(window,
                     text = "Exit",
                     command = exit)
  
# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column = 1, row = 1)
  
button_explore.grid(column = 1, row = 2)
  
button_exit.grid(column = 1,row = 3)
  
# Let the window wait for any events
window.mainloop()
