"""Copy MP3 files given a certain length (in seconds) from source path to destination path.
    
Usage:
    
    Python3 copyMP3.py
"""
from tkinter import *
from tkinter import ttk
import os, shutil
from mutagen.mp3 import MP3


def gui_find_all_mp3_files(*args):
    """Finds MP3 files in the user inputted directory, selects MP3 files based on user inputted lengths (in seconds), makes a copy of MP3 files to the user inputted path.
    """
    try:
        original_path = original_music_path.get() # Convert user entered source path to usable string
        target_path = target_music_path.get() # Convert user entered destination path to usable string
        extension = extension_variable.get()
        for root, dirs, files in os.walk(original_path): 
            for file in files:
                file_string = root+"/"+file
                if file.endswith((".mp3")):
                    try:
                        min_song_length = float(minimum_song_length.get()) # Convert user entered length to usable float
                        max_song_length = float(maximum_song_length.get()) # Convert user entered length to usable float
                    except:
                        audio_string = root+"/"+file # Create the exact path to the file by combining the root plus a slash and the file.mp3 name
                        audio = MP3(audio_string) # Use path to specific MP3 file and store it as an MP3 variable
                        audio_length_in_secs = audio.info.length # Use .info.length to convert the MP3 variable to an interger containing the amount of seconds the MP3 file is
                        try:
                            if audio_length_in_secs >= min_song_length and audio_length_in_secs <= max_song_length: # If statement to allow user to select range of file lengths user wants to copy to the given destination
                                shutil.copy(audio_string,target_path) # Copy files from root entered path to user entered destination path
                                print(f'The ".mp3" file: "{file}" has been copied to the folder: "{target_path}"\nThe ".mp3" file: "{file}" has a length of {audio_length_in_secs:.2f} seconds.') # Display message to user of the name of the files copied over, the target destination they were copied over to, and the length of the song that was copied over. 
                        except:
                            if file.endswith((f'.{extension}')):
                                file_string = root+"/"+file
                                shutil.copy(file_string,target_path) # Copy files from root entered path to user entered destination path
                                print(f'The "{extension}" file: "{file}" has been copied to the folder: "{target_path}"')
                else:
                    if file.endswith((f'.{extension}')):
                                file_string = root+"/"+file
                                shutil.copy(file_string,target_path) # Copy files from root entered path to user entered destination path
                                print(f'The "{extension}" file: "{file}" has been copied to the folder: "{target_path}"')
    except:
        pass

root = Tk()
root.title("File Sorter")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, columnspan=3, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

original_music_path = StringVar()
ttk.Label(mainframe, text="Enter path to copy files from: ").grid(column=0, row=1)
original_music_path_entry = ttk.Entry(mainframe, width=35, textvariable=original_music_path).grid(column=1, row=1, sticky=(W, E))

target_music_path = StringVar()
ttk.Label(mainframe, text="Enter path to copy files to: ").grid(column=0, row=2)
target_music_path_entry = ttk.Entry(mainframe, width=10, textvariable=target_music_path).grid(column=1, row=2, sticky=(W, E))

minimum_song_length = StringVar()
ttk.Label(mainframe, text="Enter minimum length of song (in seconds): ").grid(column=1, row=3)
minimum_song_length_entry = ttk.Entry(mainframe, width=10, textvariable=minimum_song_length).grid(column=2, row=3, sticky=(W, E))

maximum_song_length = StringVar()
ttk.Label(mainframe, text="Enter maximum length of song (in seconds): ").grid(column=1, row=4)
maximum_song_length_entry = ttk.Entry(mainframe, width=10, textvariable=maximum_song_length).grid(column=2, row=4, sticky=(W, E))

extension_variable = StringVar()
ttk.Label(mainframe, text="Enter the extension type you want to copy over. (ex: jpg): ").grid(column=1, row=6)
extension_variable_entry = ttk.Entry(mainframe, width=10, textvariable=extension_variable).grid(column=2, row=6, sticky=(W, E))

ttk.Button(mainframe, text="Copy files", command=gui_find_all_mp3_files).grid(column=1, row=5, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=2)
    
root.mainloop()