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
ffmpeg_7z_path = './ffmpeg.7z'
ffmpeg_exe_path = './ffmpeg.exe'

# ffmpeg.7z 파일이 존재하는지 확인합니다.
if os.path.isfile(ffmpeg_7z_path) == True:
    # ffmpeg.exe 파일이 존재하지 않는지 확인합니다.
    if os.path.isfile(ffmpeg_exe_path) == False:
        try:
            # 7za 명령 줄 유틸리티를 사용하여 .exe 파일을 추출합니다.
            # 시스템 구성에 따라 7za의 경로를 조정해야 할 수 있습니다.
            subprocess.run([r"C:\Program Files\7-Zip\7z.exe", 'e', ffmpeg_7z_path, '-o./', 'ffmpeg.exe'], check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            # 압축 해제가 실패한 경우 오류 메시지를 출력하고 프로그램을 종료합니다.
            print("파일 압축 해제에 실패했습니다.")
            sys.exit("Failed to extract the file.")
    # 다시 한번 ffmpeg.exe 파일이 존재하는지 확인합니다. 
    if os.path.isfile(ffmpeg_exe_path) == False:
        # 만약 여전히 없다면 오류 메시지를 출력하고 프로그램을 종료합니다.
        print("ffmpeg.exe 파일이 존재하지 않습니다.")
        sys.exit("Failed to find ffmpeg.exe.")
    # 마지막으로, 원본인 ffmpeg.7z 파일이 아직도 있는 경우 이를 삭제합니다. 
    if os.path.isfile(ffmpeg_7z_path) == True:
        os.remove(ffmpeg_7z_path)

# title 출력
print(title+"\n")

# 다운로드할 플레이리스트 URL
url = str(input("Please enter url: "))
download_playlist(url)
