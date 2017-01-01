#imports
import os
import shutil

class py2exe:
    def __init__(self, filename):
        self.filename = filename

    def pre_install(self):
        #---using this for posthandling---#
        global maindir
        maindir = os.getcwd()


    def installing(self):
        os.chdir(os.path.join(os.getcwd(),"tools", "PyInstaller-3.2"))
        print("creating exe file..")
        os.system("python " + "pyinstaller.py " + os.path.join(maindir,"input", self.filename) + " -y")

        print(self.filename)

    def posthandling(self):
        #---moving stuff and such---#
        print("moving to output folder..")
        shutil.move(self.filename[:-3], os.path.join(maindir, "output"))
        print("cleaning up..")
        #using rmdir instead of del to supress prompt#
        os.system("rmdir " + os.path.join(maindir, "output", self.filename[:-3],"build") + " /s /q")
        os.system("del /f " + os.path.join(maindir, "output", self.filename[:-3], self.filename[:-3] + ".spec"))
        print("after the first one, i'm here!")
        print(os.getcwd())
        os.chdir("..")
        os.chdir("..")
