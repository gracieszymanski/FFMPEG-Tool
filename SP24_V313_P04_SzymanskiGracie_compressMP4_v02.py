#################################
# SP24_V313_P04_SzymanskiGracie_compressMP4_v02.py
# Takes mp4 files from a file folder and compresses them based on user input
# by Gracie Szymanski, VSFX-313
# Created:  4/13/24 Modified: 4/30/24
#################################

import os
import ffmpeg_utils02

#A function that checks for errors from the file folder
def check_folder_content(list_dir): 

    if len(list_dir) == 0: #if the folder is empty, an error message appears
        print("Error: File folder is empty")
        
    for file in list_dir: 
        breakdown = os.path.splitext(file) #splits the file name into parts based on the periods

        #checks to see if there are any other types of files in the folder besides mp4s
        if breakdown[1] != ".mp4":
            print("Error: Non mp4 files in folder")
    


#The main function that defines the parts of the command and then runs the ffmpeg command
def main(path, comp_amt, compress_size_one, compress_size_two, compress_output_path):

    list_dir = os.listdir(path) #uses os.listdir to get a list of the files in the folder
    
    #runs the functions that check for errors
    check_folder_content(list_dir)

    #grabs information from the list directory to properly define variables
    for file in list_dir:
        breakdown = os.path.splitext(file)
        name = os.path.join(path, breakdown[0])
        new_path = os.path.join(compress_output_path, breakdown[0])

        #if statement to determine if user wanted to change size, then properly defines size variable
        if int(compress_size_one) == 0:
            size = " "

        else:
            size = " "
            size = (f" -s {compress_size_one}:{compress_size_two} ")

        #calls ffmpeg_utils file to create the command that compresses mp4s in ffmpeg
        command = ffmpeg_utils02.compress_mpeg(name, comp_amt, size, new_path)

        #runs the command
        os.system(command)
    
    print("Mp4's Have Been Compressed!")



if __name__ == "__main__":
    #runs the main function
    main(compress_path, comp_amt, compress_size_one, compress_size_two, compress_output_path)
