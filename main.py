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
|           Youtube mp3 Downloader  V: 2.4.2  |
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


# 플레이리스트 다운로드 함수, save_path 인자 추가
def download_playlist(url, save_path): 
    ydl_opts = {
        'format': 'bestaudio/best',                       # 영상화질 선택(화질을 선택하지 않으면 가장 좋은 화질로 다운로드)
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',      # 다운로드 경로 설정, save_path 사용
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


# 터미널 화면 지우기
def clear():
    if '\\' in os.getcwd():
        os.system('cls')
    else:
        os.system('clear')


# 파이썬 기본 모듈
try:
    import subprocess
    import sys
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


if os.path.isfile(ffmpeg_7z_path) == True:            # ffmpeg.7z 파일이 존재하는지 확인
    
    if os.path.isfile(ffmpeg_exe_path) == False:      # ffmpeg.exe 파일이 존재하지 않는지 확인
        try:
            subprocess.run(["./7-Zip/7z.exe", 'e', ffmpeg_7z_path, '-o./', 'ffmpeg.exe'], check=True)     # .exe 파일을 추출
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("파일 압축 해제에 실패했습니다.")
            sys.exit("Failed to extract the file.")   # 파일 압축 해제 실패시 오류 메시지 출력 후 종료
    if os.path.isfile(ffmpeg_exe_path) == False:      # ffmpeg.exe 파일이 존재 확인 
        print("ffmpeg.exe 파일이 존재하지 않습니다.")
        sys.exit("Failed to find ffmpeg.exe.")        # ffmpeg.exe 파일이 존재하지 않는 경우 오류 메시지 출력 후 종료
    if os.path.isfile(ffmpeg_7z_path) == True:        # ffmpeg.7z 파일이 있는 경우 삭제
        os.remove(ffmpeg_7z_path)

if __name__ == "__main__":
    
    from gui import start_gui
    
    clear()
    
    print(title + "\n")
    
    start_gui()  