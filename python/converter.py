
#from pydub import AudioSegment as segment
import os
import shutil

inputformat = "3gpp"
outputformat = "mp3"
inputdir = "./output/"
outputdir = "./output/mp3s/"

if not os.path.exists(outputdir):
    os.mkdir(outputdir)

files = os.listdir(inputdir)
gppfiles = [file for file in files if "."+inputformat in file]
print("List of", inputformat, "files found in", inputdir, ":")
print(gppfiles)

for file in gppfiles:
    shutil.copy(inputdir+file, outputdir+file.replace(inputformat, outputformat))
    #audio = segment.from_file(file=outputdir+file, format=inputformat)
    #audio.export(outputdir+file.replace(inputformat, outputformat), format=outputformat)