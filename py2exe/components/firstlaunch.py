#imports
import os
import zipfile

import wget


class firstlaunch:
    def __init__(self, url):
     self.url = url

    def setup(self):
        global maindir
        maindir = os.getcwd()
        if not os.path.exists(os.path.join(os.getcwd(),"input")):
             os.mkdir(os.path.join(os.getcwd(),"input"))
        if not os.path.exists(os.path.join(os.getcwd(),"output")):
             os.mkdir(os.path.join(os.getcwd(),"output"))
        if not os.path.exists(os.path.join(os.getcwd(),"pyinstaller")):
             os.mkdir(os.path.join(os.getcwd(),"pyinstaller"))

    def download(self):
        os.chdir(maindir)
        if os.path.isfile('pyinstaller.zip') != True:
            print('downloading files..')

            wget.download(self.url, 'pyinstaller.zip')

        if os.path.isfile('PyInstaller-3.2') != True:
            print("preparing files..")
            zip = zipfile.ZipFile('pyinstaller.zip')
            zip.extractall()
            print("done.")



