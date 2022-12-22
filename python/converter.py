
#from pydub import AudioSegment as segment
import os
#import shutil
import moviepy.editor as me

inputformat = "3gpp"
outputformat = "mp3"
inputdir = "./output/"
outputdir = "./output/mp3s/"

if not os.path.exists(outputdir):
    os.mkdir(outputdir)

files = os.listdir(inputdir)
inputfiles = [file for file in files if "."+inputformat in file]

for file in inputfiles:
    path = inputdir+file
    print("Converting file", file)
    audio = me.AudioFileClip(path)
    audio.write_audiofile(outputdir+file.replace(inputformat, outputformat))
    print("Conversion done; proceeding\n")

print("Finished!")