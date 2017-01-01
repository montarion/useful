from components.firstlaunch import firstlaunch
from components.py2exe import py2exe

init = firstlaunch("https://github.com/pyinstaller/pyinstaller/releases/download/v3.2/PyInstaller-3.2.zip")

init.download()

install = py2exe("network-drives(windows.py")
install.pre_install()
install.installing()
install.posthandling()

install = py2exe("anime-tracker.py")
install.pre_install()
install.installing()
install.posthandling()
