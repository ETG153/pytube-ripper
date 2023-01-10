from pytube import Playlist as pl

listurl = "https://www.youtube.com/playlist?list=PLd2hJYgWor6CK2MgmoDmtqfq9H4cTm9FN"
outputdir = "./output/"
minruntime = 120

print("Fetching playlist...")
while True:
    try:
        list = pl(url=listurl)
    except ConnectionResetError:
        print("Connection reset")
    else:
        print("Success!\n")
        break

print("Fetching title...")
while True:
    try:
        title = list.title
    except ConnectionResetError:
        print("Connection reset")
    else:
        print("Success!\n")
        break

print("Fetching video list...")
while True:
    try:
        videos = list.videos
    except ConnectionResetError:
        print("Connection reset")
    else:
        print("Success!\n")
        break

print("Playlist title:", title, "\n")

for video in videos:
    print("Fetching video length...")
    while True:
        try:
            vidlength = video.length
        except ConnectionResetError:
            print("Connection reset")
        else:
           print("Success!\n")
           break
    
    print("Fetching video title...")
    while True:
        try:
            vidtitle = video.title
        except ConnectionResetError:
            print("Connection reset")
        else:
           print("Success!\n")
           break

    print("Title:", vidtitle, ", Length:",vidlength)
    if vidlength >= minruntime:
        print("Applying filter...")
        while True:
            try:
                video.streams.filter(only_audio=True)
            except ConnectionResetError:
                print("Connection reset")
            else:
               print("Success!\n")
               break

        print("Downloading video...")
        while True:
            try:
                video.streams.first().download(output_path = outputdir)
            except ConnectionResetError:
                print("Connection reset")
            else:
               print("Success!\n")
               break
        
    else:
        print("Too short")