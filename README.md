# FFMPEG Tool and GUI

# Project Objectives:

 # ★ Create and connect a GUI, using QtDesigner, to an FFMPEG tool that converts stills to mp4 or compresses mp4s.
 # ★ Code should gather inputs from the GUI and use it to execute the FFMPEG 
# command to combine stills to an MP4 or compress mp4s.
 
# My GUI:
 
#  ★ Has two different tabs so that the app can turn stills into MP4s and 
# compress MP4s.
#  ★ Includes an option to resize output files.
#  ★ For the stills, includes area to customize the name of the output MP4.
#  ★ Includes area to output the file to a specific folder so it is not confined to the same folder the files came from.
#  ★ Spin boxes are bound to certain numbers such as 52 being the highest for compression
#  ★ Includes a description at the top for how the app works.
#  ★ Includes labels throughout to help with user interface design and make 
# the app as clear as possible.
#  ★ Includes labels that update with the current selected folder

# Features:

#  ★ By clicking yes or no on the resize question, the user triggers the signal that will make new size 
# widgets appear.
#  ★ This way, size inputs are not cluttering up the GUI if the user does not choose to resize the file.
#  ★ The run button is disabled until the user gives the GUI the input and 
# output folders.
#  ★ This reduces user error a bit. 
#  ★ Once users input two files then the run button is enabled
