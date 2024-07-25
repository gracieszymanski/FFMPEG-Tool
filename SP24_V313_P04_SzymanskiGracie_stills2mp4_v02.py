#################################
# SP24_V313_P04_SzymanskiGracie_stills2mp4_v02.py
# Takes stills from a file folder and turns them into an mp4 using ffmpeg
# by Gracie Szymanski, VSFX-313
# Created:  4/7/24 Modified: 4/30/24
#################################

import os
import ffmpeg_utils01


#A function that checks for errors from the file folder
def check_folder_content(list_dir): 

    #creates set used in the function
    extensions = set()

    if len(list_dir) == 0: #if the folder is empty, an error message appears
        print("Error: File folder is empty")
        
    for file in list_dir: 

        file_breakdown = os.path.splitext(file) #splits the file name into parts based on the periods

        #adds extension of files and names of files to a set
        extensions.add(file_breakdown[1])

        #uses sets to see if there are multiple kinds of file extentions or multiple different names of files in the folder
        if len(extensions) > 1:
            print("Error: Multiple image types in the folder.")



#The main function that difines the parts of the command and then runs the ffmpeg command
def main(stills_path, speed, stills_size_one, stills_size_two, stills_output_path, stills_input_name):
    list_dir = os.listdir(stills_path) #uses os.listdir to get a list of the files in the folder
    
    #runs the functions that check for errors
    check_folder_content(list_dir)

    #grabs information from the list directory to properly define variables
    breakdown = list_dir[0].split(".") #splits a file from the folder by periods to grab each individual part
    digits = len(breakdown[1])
    image_type = breakdown[2]
    name = os.path.join(stills_path, breakdown[0])
    video_name = os.path.join(stills_output_path, stills_input_name)

    #if statement to determine if user wanted to change size, then properly defines size variable
    if int(stills_size_one) == 0:
        size = " "

    else:
        size = " "
        size = (f" -s {stills_size_one}:{stills_size_two} ")

    #calls ffmpeg_utils file to create the command for ffmpeg
    command = ffmpeg_utils01.seq_to_mpeg(name, image_type, speed, digits, size, video_name)

    #runs the command
    os.system(command)

    print("Done with MP4!")



if __name__ == "__main__":
    #runs the main function
    main(stills_path, speed, stills_size_one, stills_size_two, stills_output_path, stills_input_name)
