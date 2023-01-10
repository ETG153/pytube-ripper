
import os
import sys
import getopt
from pytube import Playlist as pl
from pytube import YouTube as yt
from pytube import exceptions
import moviepy.editor as me

# Usage: set source URL with -s, destination path with -o, and -c to convert files to mp3.

def main(arguments):
    outdir = "./outputs/" # default output directory
    sourceurl = "\0"
    isplaylist = False
    runconversion = False

    print("Pytube downloader + converter CLI tool v1.0")
    
    flags, options = getopt.getopt(args=arguments, shortopts="s:o:c")
    for flag, option in flags:

        if flag == "-s":
            sourceurl = option
            if "list=" in sourceurl:
                isplaylist = True
        
        elif flag == "-o":
            outdir = option
        
        elif flag == "-c":
            runconversion = True
    
    print("Source url:", sourceurl)
    print("Source is a playlist:", isplaylist)
    print("Output directory:", outdir, "\n")
    
    if isplaylist:
        print("Fetching playlist info...")
        while True:
            try:
                playlist = pl(url=sourceurl)
            except ConnectionResetError:
                print("Connection reset, retrying...")
            else:
                print("Success!\n")
                break
        
        print("Fetching video list...")
        while True:
            try:
                videos = playlist.videos
            except ConnectionResetError:
                print("Connection reset, retrying...")
            else:
                try:
                    list(videos)
                except KeyError:
                    sys.exit("Invalid playlist URL!")
                except ConnectionResetError:
                    continue
                else:
                    print("Success!\n")
                    break
    
    else:
        print("Fetching video info...")
        while True:
            try:
                videos = [yt(url=sourceurl)]
            except ConnectionResetError:
                print("Connection reset, retrying...")
            except exceptions.RegexMatchError:
                sys.exit("Invalid video URL!")
            else:
                print("Success!\n")
                break
    
    print("Starting download(s)")
    for video in videos:
        if runconversion:
            videopath = outdir+"temp/"
        else:
            videopath = outdir
        print("Downloading item...")
        while True:
            try:
                video.streams.get_highest_resolution().download(output_path = videopath)
            except ConnectionResetError:
                print("Connection reset, retrying...")
            else:
               print("Success!\n")
               break

    if not runconversion:
        print("Finished!")
        if __name__ == "__main__":
            sys.exit()
        else:
            return
    
    print("Done!\n")
    
    print("Running conversions...")
    videofiles = os.listdir(videopath)
    filteredfiles = []

    for file in videofiles:
        filename, extension = file.rsplit(sep=".", maxsplit=1)
        if not any(filename in files for files in filteredfiles):
            filteredfiles.append(file)

    for file in filteredfiles:
        audio = me.AudioFileClip(videopath+file)
        fileformat = file.rsplit(sep=".", maxsplit=1)[1]
        audio.write_audiofile(outdir+file.replace(fileformat, "mp3"))
    print("Done!\n")

    print("Cleaning up...")
    for file in videofiles:
        print("Removing", str(file)+"...")
        os.remove(videopath+file)
    print("Removing temp directory...")
    os.rmdir(videopath)
    print("Finished!")

if __name__ == "__main__":
    main(sys.argv[1:])
