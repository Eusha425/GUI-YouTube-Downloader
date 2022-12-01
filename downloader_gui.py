from tkinter import *
from tkinter import ttk
import youtube_video_downloader as ytd
from PIL import ImageTk, Image
import time

first_click = True
progress_display = True

# sending the user input to the youtube downloader
def send_link():
    progress.place(y = 180, x = 125)     # display the progress bar for visual representation of the download 
    youtube_link = name_entry.get()   # getting the user input youtube video link
    ytd.yt_download(youtube_link)    # passing the link to the downloader 
    progress_bar()                   # calling the progress bar to add value to it

# deleting user input in the entry widget and resetting progress bar
def reset_entry():
    global progress_display
    name_entry.delete(0 , 'end')       # deleting existing text in the entry widget
    progress["value"] = 0           # resetting progress value to 0
    if progress_display:             # hiding the progress bar again
        progress.place_forget()

# progress bar update
def progress_bar():
    # incrementing value to the progress bar
    for i in range(5):
        progress['value'] += 20
        window.update_idletasks()
        time.sleep(1)

# for the temporary text on the entry widget when the user is clicking the entry widget for the first time   
def on_entry_click(event):   
    global first_click
    if first_click: # if this is the first time they clicked it
        first_click = False
        name_entry.delete(0, "end") # delete all the text in the entry

# tkinter object called window
window = Tk()
# resizing the window
window.geometry("500x450")
# creating a frame for the picture
frame = Frame(window, width=600, height=400)
frame.pack()
# setting the spot of the widget to center and the horizontal and vertical offset to 0.5 of the parent widget i.e (the window)
frame.place(anchor = 'center', relx = 0.5, rely = 0.5)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("youtube.png"))

# Create a Label Widget to display the Image
label = Label(frame, image = img)
label.pack()

# renaming the program window from the default tk
window.title("Youtube Downloader")

# setting up labels widget for user input
label = Label(window ,borderwidth = 3, relief = RAISED, text = "Welcome to the YouTube Downloader!", font=("Arial", 15), background = "black", foreground = "white")
label.pack(pady = "10")

# entry label message and user entry
name_entry = Entry(relief = SUNKEN, background = "#C0C0C0")
name_entry.insert(0, 'Enter YouTube Video link...')
name_entry.bind('<FocusIn>', on_entry_click)

# relocating the widgets from the default position
name_entry.place(y = "50", x = "185", width = 165, height = 23)

# progressbar 
progress = ttk.Progressbar(window, orient = 'horizontal', mode = 'determinate', length = 280)

# submit button
submit_button = Button(text = "Submit", borderwidth = 2, relief = RIDGE, width = "10", height = "1", command = send_link)
submit_button.place(y="80",x="325")

# download again button
reset_button = Button(text = "Download Again?", borderwidth = 2, relief = RIDGE, width = "15", height = "1", command = reset_entry)
reset_button.place(y="80",x="105")

# author label
author_label = Label(window,borderwidth=3,relief=RAISED, text="Author: Gazi Eusha", font=("Arial", 15),background="black",foreground="white")
author_label.place(y=345,x=10)

# exit button
exit_button = Button(text="EXIT",borderwidth = 2, relief = RAISED,font=("Arial", 12, "bold"), width="7", height="1",background="red",fg="black",command=window.destroy)
exit_button.place(y=345,x=410)

window.mainloop()