import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["os", "cv2", "PySimpleGUI", "pytube", "tkinter"],
    "include_files": [
        "yt.mp4",
        "yt1.ico",
        "tcl86t.dll",
        "tk86t.dll"
    ],
    "excludes": ["tkinter"],
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="YouTube Video Downloader",
    version="0.1",
    description="Downloads YouTube videos",
    options={"build_exe": build_exe_options},
    executables=[
        Executable("main.py", base=base)
    ]
)
