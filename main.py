# title
title ="""
 _____________________________________________
|                                             |
| MADE BY                                     |
|     _________    ___    ___   _________     |
|    |   ______|   \  \  /  /  |___    __|    |
|    |  |______     \  \/  /       |  |       |
|    |_______  |     \    /        |  |       |
|     _______| |      |  |       __|  |       |
|    |_________|      |__|      \_____/       |
|                                             |
|                                    2.0.0    |
|_____________________________________________|
"""

import yt_dlp

def download_playlist(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'ffmpeg_location': 'C:/ffmpeg/bin/ffmpeg.exe',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            }],
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# title 출력
print(title+"\n")

# 다운로드할 플레이리스트 URL
url = str(input("Please enter url: "))
download_playlist(url)
