#imports
import os
import shutil
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
        if not os.path.exists(os.path.join(self.maindir,"tools")):
             os.mkdir(os.path.join(self.maindir,"tools"))

    def download(self):
        os.chdir(self.maindir)
        if not os.path.exists(os.path.join("tools", "pyinstaller-3.2")):
            print('downloading files..')

            wget.download(self.url, 'pyinstaller.zip')
            print("download complete.")

        if not os.path.exists(os.path.join("tools", "pyinstaller-3.2")):
            print("preparing files..")
            zip = zipfile.ZipFile('pyinstaller.zip')
            zip.extractall()
            print("done.")

        if not os.path.exists(os.path.join("tools", "pyinstaller-3.2")):
            print("doing this!")
            shutil.move(os.path.join(self.maindir, "pyinstaller-3.2"), os.path.join(self.maindir, "tools"))

        if os.path.isfile("pyinstaller.zip") == True:
            os.system("del pyinstaller.zip")


