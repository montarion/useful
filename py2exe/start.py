import os
from time import sleep

from components.firstlaunch import firstlaunch
from components.py2exe import py2exe

#---url==link to pyinstaller---#
url = "https://github.com/pyinstaller/pyinstaller/releases/download/v3.2/PyInstaller-3.2.zip"
#---req check---#
filename = "anime-tracker.py"

#filename = input("what is the file that you want to convert?")
if not os.path.exists(os.path.join(os.getcwd(), "input")):


    init = firstlaunch(url)

if not os.path.exists(os.path.join(os.getcwd(), "tools", "PyInstaller-3.2")):

    firstlaunch(url).download()


if not os.path.isfile(os.path.join(os.getcwd(), "input", filename)):
    print("please place", filename, "in the input folder and run the program again.")
    sleep(3)
    os.system("explorer " + os.path.join(os.getcwd(), "input"))

else:
    install = py2exe(filename)
    install.installing()
    install.posthandling()

