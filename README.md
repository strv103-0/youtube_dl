# 유튜브 MP3 파일 다운로드 프로그램


## 사용법
> 1. 파이썬 파일과 같은 위치에 **downloads**폴더를 추가한다.
> 2. 터미널을 열고 `pip install yt-dlp`를 입력한다.
> 3. [ffmpeg 설치 가이드](#ffmpeg-설치-가이드windows-버전)에 따라 ffmpeg를 설치한다.
> 4. 파이썬 파일을 실행한다.
> 5. 유튜브 **플레이리스트** URL을 입력한다.
> 6. **downloads** 폴더에서 파일을 가져온다.



## 버전
> - 1.0.0 플레이리스트 다운로드
> - 1.1.0 실패한 다운로드, 변환 파일 목록 출력
> - 1.1.1 path 버그 수정
> - 1.2.1 라이브러리 자동설치
> - 2.0.0 **pytube** 에서 **yt_dlp**로 라이브러리 변경



## 개발 중인 기능
> - .py파일을 .exe로 제작
> - ffmpeg 자동 설치
> - 라이블러리 자동 설치



## **ffmpeg** 설정 가이드(Windows 버전)
### 다운로드 실패시 [**ffmpeg** 설치 가이드(공식 사이트)](#ffmpeg-설치-가이드공식-사이트)로 이동
> 1. `ffmpeg.7z` 파일을 `C:/`에 압축을 해제한다.
> 2. 시스템 환경 변수 편집에 들어가 **환경 변수** 버튼을 누르고 **Path**을 누르고 **편집**을 누른다.![image](https://github.com/strv103-0/youtube_dl/assets/112059527/83368f86-c7d9-484a-b450-81a6cdc72f3f)
> 3. **새로 만들기**를 누른후 `C:\ffmpeg\bin`을 입력하고 저장하면 설정 끝이다.![image](https://github.com/strv103-0/youtube_dl/assets/112059527/83ca66aa-c5a2-4d7f-b054-d1d0531917c5)



## **ffmpeg** 설치 가이드(공식 사이트)
> 1. [**FFmpeg** 다운로드 페이지](https://ffmpeg.org/download.html)로 들어간다.
> 2. **Windows** 이미지를 누른다. ![image](https://github.com/strv103-0/youtube_dl/assets/112059527/710c066e-eea6-4102-8e67-f4831e57ae49)
> 3. `Windows builds from gyan.dev`버튼을 누른다.![image](https://github.com/strv103-0/youtube_dl/assets/112059527/293ad0ca-28ad-4ed4-9aa6-f2f94897276f)
> 4. `ffmpeg-git-full.7z`를 눌러 파일을 다운로드 한다.![image](https://github.com/strv103-0/youtube_dl/assets/112059527/e56046fa-ce7a-4e40-bf76-6c0cf74bcc97)
> 5. 다운로드 후 파일을 `C:/`에 압축을 해제한다.
> 6. 시스템 환경 변수 편집에 들어가 **환경 변수** 버튼을 누르고 **Path**을 누르고 **편집**을 누른다.![image](https://github.com/strv103-0/youtube_dl/assets/112059527/83368f86-c7d9-484a-b450-81a6cdc72f3f)
> 7. **새로 만들기**를 누른후 `C:\ffmpeg\bin`을 입력하고 저장하면 설정 끝이다.![image](https://github.com/strv103-0/youtube_dl/assets/112059527/83ca66aa-c5a2-4d7f-b054-d1d0531917c5)