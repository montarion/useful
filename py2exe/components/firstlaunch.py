#imports
import os
import zipfile

import wget


class firstlaunch:
    def __init__(self, url):
        self.url = url
        self.maindir = os.getcwd()

        if not os.path.exists(os.path.join(self.maindir,"input")):
             os.mkdir(os.path.join(self.maindir,"input"))
        if not os.path.exists(os.path.join(self.maindir,"output")):
             os.mkdir(os.path.join(self.maindir,"output"))
        if not os.path.exists(os.path.join(self.maindir,"pyinstaller")):
             os.mkdir(os.path.join(self.maindir,"pyinstaller"))

    def download(self):
        os.chdir(self.maindir)
        if os.path.isfile('pyinstaller.zip') != True:
            print('downloading files..')

            wget.download(self.url, 'pyinstaller.zip')

        if os.path.isfile('PyInstaller-3.2') != True:
            print("preparing files..")
            zip = zipfile.ZipFile('pyinstaller.zip')
            zip.extractall()
            print("done.")



