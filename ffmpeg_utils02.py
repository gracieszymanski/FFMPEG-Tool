#################################
# ffmpeg_utils02.py
# by Gray Marshall, VSFX-313
# Created:  09/10/22
# Modified: 04/30/24 by Gracie Szymanski for FFMPEG GUI
#################################

import os

PATH = "./test"  # TEMP testing path

FFMPG_PARAMS_SEQ = '-s 960:540 -codec:v libx264 '  # Resizes to 960x540 AND uses H264
FFMPG_PARAMS_CMP = '-y -codec:v libx264 '  # Auto-overwrites output file AND uses H264


def seq_to_mpeg(name, image_type, speed, digits):
    command = f'ffmpeg -i {name}.%0{digits}d.{image_type} {FFMPG_PARAMS_SEQ}'\
            + f'-r {speed} {name}.mp4'
    return command


def compress_mpeg(name, comp_amt, size, new_path):
    r"""
    Creates command string for ffmpeg to compress MP4 to
    a different amount

    Inputs:
        name: str - Path & Basename of file to convert. Should
                    NOT include extension.
                    Example:
                    D:\user\fred\files\movies\my_movie
        comp_amt: int - Amount of Compression;
                    0 = Lossless Comp, 51 = Most Comp
                    17 - 28 is considered sane, 23 is default

    Return:
        Full executable command string as string
    """

    command = f'ffmpeg -i \"{name}.mp4\"{size}{FFMPG_PARAMS_CMP}'\
            + f'-crf {comp_amt} \"{new_path}_CMP.mp4\"'
    return command


# Just for testing
if __name__ == "__main__":
    curr_os = os.name
    print(f"Current OS: {curr_os}")

    os.system("ffmpeg -version")
    print(compress_mpeg(PATH, 20))
