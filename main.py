# title
title ="""
 _____________________________________________
|                                             |
| MADE BY                                     |
|     _________    ___    ___   _________     |
|    |   ______|   \  \  /  /  |___    __|    |
|    |  |______     \  \/  /       |  |       |
|    |_______  |     \    /        |  |       |
|     _______| |      |  |      ___|  |       |
|    |_________|      |__|      \_____/       |
|                                             |
|                                    2.1.0    |
|_____________________________________________|
"""

import subprocess
import sys

def install(package):
    try:
        # 파이썬 import 문을 사용하여 모듈 존재 확인
        __import__(package)
    except ImportError:
        # 모듈이 없으면 pip를 사용하여 설치
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# yt_dlp 라이브러리를 체크하고 필요시 설치합니다.
install('yt_dlp')

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
