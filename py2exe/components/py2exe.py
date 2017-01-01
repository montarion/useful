#imports
import os
import shutil
from time import sleep

class py2exe:
    def __init__(self, filename):
        self.filename = filename

        #---using this for posthandling---#

        self.maindir = os.getcwd()


    def installing(self):
        os.chdir(os.path.join(os.getcwd(),"tools", "PyInstaller-3.2"))
        print("converting " + self.filename + " to exe..")
        os.system("python " + "pyinstaller.py " + os.path.join(self.maindir,"input", self.filename) + " -y")



    def posthandling(self):
        #---moving stuff and such---#
        print("moving to output folder..")
        shutil.move(self.filename[:-3], os.path.join(self.maindir, "output"))
        print("cleaning up..")
        #using rmdir instead of del to supress prompt#
        print(self.maindir)
        os.system("rmdir " + os.path.join(self.maindir, "output", self.filename[:-3],"build") + " /s /q")
        os.system("del /f " + os.path.join(self.maindir, "output", self.filename[:-3], self.filename[:-3] + ".spec"))
        print("conversion complete!")
        print("remember to create shortcuts, since the exe file has to stay in it's folder!")
        sleep(2)

        print("opening output file..")
        os.system("explorer /select, " + os.path.join(self.maindir,"output", self.filename[:-3], "dist", self.filename[:-3], self.filename[:-3] + ".exe"))
        print("explorer /select, " + os.path.join(self.maindir,"output", self.filename[:-3], "dist", self.filename[:-3], self.filename[:-3] + ".exe"))
