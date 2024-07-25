#################################
# ffmpeg_utils01.py
# by Gray Marshall, VSFX-313
# Created:  09/10/22
# Modified: 04/30/24 by Gracie Szymanski for FFMPEG GUI
#################################

import os

PATH = "./test"  # TEMP testing path

FFMPG_PARAMS = '-codec:v libx264 '


def seq_to_mpeg(name, image_type, speed, digits, size, video_name):
    command = f'ffmpeg -i {name}.%0{digits}d.{image_type}{size} {FFMPG_PARAMS}'\
            + f'-r {speed} {video_name}.mp4'
    return command


# Just for testing
if __name__ == "__main__":
    os.system("ffmpeg -version")
    print(seq_to_mpeg(PATH, "jpg", 24, 4))
