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


# 플레이리스트 다운로드 함수
def download_playlist(url):
    ydl_opts = {
        'format': 'bestaudio/best',                       # 영상화질 선택(화질을 선택하지 않으면 가장 좋은 화질로 다운로드)
        'outtmpl': 'downloads/%(title)s.%(ext)s',         # 다운로드 경로 설정
        'ffmpeg_location': 'C:/ffmpeg/bin/ffmpeg.exe',    # ffmpeg.exe 위치 지정
        'ignoreerrors': True,                             # 오류 발생시 건너뛰기
        'postprocessors': [{                              # 파일 변환
            'key': 'FFmpegExtractAudio',                  # 변환 모듈 선택
            'preferredcodec': 'mp3',                      # 파일 형식 설정
            }],
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:               # 다운로드 시작
        ydl.download([url])

# title 출력
print(title+"\n")

# 다운로드할 플레이리스트 URL
url = str(input("Please enter url: "))
download_playlist(url)
