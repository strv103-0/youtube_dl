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
|           Youtube mp3 Downloader  V: 2.2.1  |
|_____________________________________________|
"""


def install(package):
        try:
            # 파이썬 import 문을 사용하여 모듈 존재 확인
            __import__(package)
        except ImportError:
            try:
                # 모듈이 없으면 pip를 사용하여 설치
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            except subprocess.CalledProcessError:
                # pip 설치 실패시 에러 메세지 출력
                print(f"pip install {package} failed.")
                sys.exit("pip install failed.")


# 플레이리스트 다운로드 함수
def download_playlist(url):
    ydl_opts = {
        'format': 'bestaudio/best',                       # 영상화질 선택(화질을 선택하지 않으면 가장 좋은 화질로 다운로드)
        'outtmpl': 'downloads/%(title)s.%(ext)s',         # 다운로드 경로 설정
        'ffmpeg_location': './ffmpeg.exe',                # ffmpeg.exe 위치 지정
        'ignoreerrors': True,                             # 오류 발생시 건너뛰기
        'postprocessors': [{                              # 파일 변환
            'key': 'FFmpegExtractAudio',                  # 변환 모듈 선택
            'preferredcodec': 'mp3',                      # 파일 형식 설정
            }],
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:               # 다운로드 시작
            ydl.download([url])
    except yt_dlp.utils.DownloadError:
        print("다운로드에 실패하였습니다.")
        sys.exit("Failed to download.")

# 파이썬 기본 모듈
try:
    import subprocess
    import sys
    import zipfile
    import os
except ImportError:
    print("파이썬 기본 모듈을 불러올 수 없습니다.")
    sys.exit("Failed to import python basic module.")

# 라이브러리를 체크하고 필요시 설치합니다.
install('yt_dlp')

# 파이썬 외부 모듈
try:
    import yt_dlp
except ImportError:
    print("파이썬 외부 모듈을 불러올 수 없습니다.")
    sys.exit("Failed to import python external module.")


# path
ffmpeg_zip_path = "ffmpeg.zip"
ffmpeg_exe_path = "ffmpeg.exe"


if os.path.isfile(ffmpeg_zip_path) == True:
    if os.path.isfile(ffmpeg_exe_path) == False:
        try:
            fantasy_zip = zipfile.ZipFile(ffmpeg_zip_path)
            fantasy_zip.extract('ffmpeg.exe', './')
            fantasy_zip.close()
        except zipfile.BadZipFile:
            print("ffmpeg.zip 파일이 손상되었습니다.")
            sys.exit("ffmpeg.zip is broken.")
    if os.path.isfile(ffmpeg_exe_path) == False:
        print("ffmpeg.exe 파일이 존재하지 않습니다.")
        sys.exit("ffmpeg.exe is not found.")
    if os.path.isfile(ffmpeg_zip_path) == True:
        os.remove(ffmpeg_zip_path)

# title 출력
print(title+"\n")

# 다운로드할 플레이리스트 URL
url = str(input("Please enter url: "))
download_playlist(url)
