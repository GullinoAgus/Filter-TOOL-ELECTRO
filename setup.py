import PyInstaller.__main__
import sys

if sys.platform == 'win32' or sys.platform == 'cygwin':
    PyInstaller.__main__.run([
        'main.py',
        '--onefile',
        '--windowed',
        '--icon=icon.png',
        '--add-data=RLC.png;.',
        '--add-data=icon.png;.'
    ])
else:
    PyInstaller.__main__.run([
        'main.py',
        '--onefile',
        '--windowed',
        '--add-data=RLC.png:.',
        '--add-data=icon.png:.'
    ])
