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
|                                    1.0.1    |
|_____________________________________________|
"""

# print title
print(title)

# variable declaration
video_list = []
url = str(input("Please enter URL: "))
path = r"C:\Users\user\Desktop\just_code\python\youtube_dl\download"
failed_download = []
failed_conversion = []
failed_deletion = []

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
        failed_deletion.append(mp4_file_path)


# 실패한 다운로드 출력
print_failed_operations(failed_download, "download")

# 실패한 변환 출력
print_failed_operations(failed_conversion, "convert")

# 실패한 삭제 출력
print_failed_operations(failed_deletion, "delete")