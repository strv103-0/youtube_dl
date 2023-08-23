import os
from pytube import Playlist
from moviepy.editor import AudioFileClip



# download playlist
def download_playlist(url, path):
    playlist = Playlist(url)
    
    for video in playlist.videos:
        try:
            stream = video.streams.get_highest_resolution()  # 가장 높은 화질의 스트림 선택
            stream.download(path)
        except Exception as e: 
            print(f"An error occurred with the following video: {video.title}")

# mp4 to mp3
def convert_mp4_to_mp3(mp4_file_path, mp3_file_path):
    try:
        audio = AudioFileClip(mp4_file_path)
        audio.write_audiofile(mp3_file_path)
    except Exception as e:
        print(f"An error occurred while converting {mp4_file_path} to MP3")

# title
title ="""
 _____________________________________________
|                                             |
| MADE BY                                     |
|     _________    ___    ___   _________     |
|    |   ______|   \  \  /  /  |__    ___|    |
|    |  |______     \  \/  /      |  |        |
|    |_______  |     \    /       |  |        |
|     _______| |      |  |        |  |___     |
|    |_________|      |__|        \_____/     |
|                                             |
|                                    1.0.0    |
|_____________________________________________|
"""

# print title
print(title)

# variable declaration
video_list = []
url = str(input("Please enter URL: "))
path = "./download"

# download playlist
download_playlist(url, path)

# List folder file names
for (root, directories, files) in os.walk(path):
    for file in files:
        if '.mp4' in file:
            video_list.append(file)

# mp4 to mp3 conversion and deletion of original mp4 files.
for video in video_list:
    mp4_file_path = os.path.join(path, video)  # using os.path.join for OS-independent paths.
    mp3_file_path = os.path.join(path, video.replace(".mp4", ".mp3"))
    
    convert_mp4_to_mp3(mp4_file_path, mp3_file_path)
    
    try: 
        os.remove(mp4_file_path)
    except Exception as e: 
        print(f"An error occurred while deleting {mp4_file_path}")
