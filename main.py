import os
import sys
import subprocess

def install(package):
    subprocess.check_call([sys.executable,'-m', 'pip', 'install', '--upgrade', 'pip'])
    # 에러 발생한 모듈 설치
    subprocess.check_call([sys.executable,'-m', 'pip', 'install', '--upgrade', package])

try:
    from pytube import Playlist
    from moviepy.editor import AudioFileClip
except:
    install('pytube')
    install('moviepy')
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
            failed_download.append(video.title)

# mp4 to mp3
def convert_mp4_to_mp3(mp4_file_path, mp3_file_path):
    try:
        audio = AudioFileClip(mp4_file_path)
        audio.write_audiofile(mp3_file_path)
    except Exception as e:
        print(f"An error occurred while converting {mp4_file_path} to MP3")
        failed_conversion.append(mp4_file_path)

# print failed operations
def print_failed_operations(failed_list, operation_type):
    if len(failed_list) > 0:
        print(f"\n\nThe following videos failed to {operation_type}:")
        for video in failed_list:
            print(video)

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
|                                    1.2.1    |
|_____________________________________________|
"""

# print title
print(title)

# variable declaration
video_list = []
path_download = "./downloads"
path_temp = "./temp"
failed_download = []
failed_conversion = []
failed_deletion = []

# url input
url = str(input("Please enter URL: "))

# download playlist
download_playlist(url, path_temp)

# List folder file names
for (root, directories, files) in os.walk(path_temp):
    for file in files:
        if '.mp4' in file:
            video_list.append(file)

# mp4 to mp3 conversion and deletion of original mp4 files.
for video in video_list:
    mp4_file_path = os.path.join(path_temp, video)  # using os.path.join for OS-independent paths.
    mp3_file_path = os.path.join(path_download, video.replace(".mp4", ".mp3"))
    
    convert_mp4_to_mp3(mp4_file_path, mp3_file_path)
    
    try: 
        os.remove(mp4_file_path)
    except Exception as e: 
        print(f"An error occurred while deleting {mp4_file_path}")
        failed_deletion.append(mp4_file_path)


# Failed download output
print_failed_operations(failed_download, "download")

# Failed conversion output
print_failed_operations(failed_conversion, "convert")

# Failed delete output
print_failed_operations(failed_deletion, "delete")
