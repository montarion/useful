#imports
import os
import shutil
import zipfile
from time import sleep

import wget


def download():

    url = 'https://github.com/pyinstaller/pyinstaller/releases/download/v3.2/PyInstaller-3.2.zip'

    if os.path.isfile('pyinstaller.zip') != True:
        print('downloading files..')
        wget.download(url, 'pyinstaller.zip')
    else:
        print("already here")
    if os.path.isfile('PyInstaller-3.2') != True:
        print("preparing files..")
        zip = zipfile.ZipFile('pyinstaller.zip')
        zip.extractall()
        print("done.")
    else:
        print('already here')




def setup():
    #---filenames
    #installdir = input("where is your PyInstaller directory? ")
    #pythonfileq = input("what file do you want to make into an exe? ")
    global pythonfile
    pythonfile = "anime-tracker.py"
    installdir = "PyInstaller-3.2"
    #pythonfile = pythonfileq
    print(pythonfile)

    workdir = os.path.join(installdir, pythonfile[:-3])
    global exefile
    exefile = os.path.join(workdir, "dist", pythonfile[:-3], pythonfile[:-3]+".exe" )
    global workfile
    workfile = os.path.join("python-files", pythonfile[:-3])
    print(workfile)
    #---filenames---#

    #s.chdir(installdir)
    print(installdir)

    ls = os.popen("dir")
    print(ls.read())

    print("creating folders..")

    try:
        os.mkdir(workdir)

    except:

        os.getcwd()



    os.chdir(installdir)

    ls = os.popen("dir")
    print(ls.read())

    try:
        os.mkdir("python-files")
    except:
        pass

    ls = os.popen("dir")
    print(ls.read())




    ls = os.popen("dir")
    print(ls.read())
    try:
        os.chdir("..")
        os.mkdir(workfile)
        os.chdir("..")
    except:
        pass


    os.getcwd()


#check to see if things have been done---#


def check():
    #---filenames---#

    #pythonfile = "anime-tracker.py"
    installdir = "PyInstaller-3.2"
    workdir = os.path.join(installdir, pythonfile[:-3])
    exefile = os.path.join(workdir, "dist", pythonfile[:-3], pythonfile[:-3]+".exe" )
    #---filenames---#

    check = os.path.isfile("check.txt")
    print(check)
    ls = os.popen("dir")
    print(ls.read())
    #os.chdir(installdir)
    if check == True:
        print("The file " + pythonfile[:-3]+".exe" + " should already exist. Opening now..")
        sleep(2)
        print(exefile)
        os.system("explorer.exe /select," + exefile)
        exit()

def installation():

    #---filenames---#

    installdir = "PyInstaller-3.2"
    workdir = os.path.join(installdir, pythonfile[:-3])
    exefile = os.path.join(workdir, "dist", pythonfile[:-3], pythonfile[:-3]+".exe" )
    truefile = os.path.join("python-files",pythonfile)
    #---filenames---#

    os.chdir("..")
    print("woop")
    os.getcwd()
    sleep(2)
    #os.rename(pythonfile,(os.path.join(installdir,"python-files")))






    if not os.path.exists(r"C:\Users\Jamiro\PycharmProjects\useful\PyInstaller-3.2\python-files"):
        os.mkdir(r"C:\Users\Jamiro\PycharmProjects\useful\PyInstaller-3.2\python-files")

    shutil.copy(os.path.join(os.getcwd(), "useful", pythonfile),os.path.join(os.getcwd(), "useful","PyInstaller-3.2", "python-files", pythonfile))
    print("working..")

    os.system("python " + os.path.join(os.getcwd(), "useful", "PyInstaller-3.2/pyinstaller.py") + " " + os.path.join(installdir, "useful" "python-files", pythonfile))

    sleep(2)
    print("done!")
    print("opening output file..")
    sleep(1)
    os.system("explorer.exe /select," + exefile)

def posthandling():
    #---filenames---#
    pythonfile = input("what file do you want to make into an exe? ")
    #pythonfile = "anime-tracker.py"
    installdir = "PyInstaller-3.2"
    workdir = os.path.join(installdir, pythonfile[:-3])
    exefile = os.path.join(workdir, "dist", pythonfile[:-3], pythonfile[:-3]+".exe" )
    #---filenames---#

    #---writing file for next use---#
    finalcheck = os.path.isfile(exefile)
    print(finalcheck)
    if finalcheck == True:
        chdir = os.chdir(workdir)
        infile = open("check.txt", "w")
        infile.write("written")
        infile.close()
        print("done with writing")

print("welcome!")
print("setting up system..")
download()
setup()
check()
installation()
posthandling()
print("there are some things that you should do first..")
print("add your python file to the 'python-files' folder")
#pythonfile = input("what file do you want to make into an exe? ")
#installdir = input("where is your PyInstaller directory? ")



print("initiating phase 2")
filedir = os.path.join(installdir, pythonfile)
print(workdir)
sleep(1)



print()
print("welcome!")
print("setting up system..")
download()
print("there are some things that you should do first..")
print("add your python file to the 'python-files' folder")
#pythonfile = input("what file do you want to make into an exe? ")
#installdir = input("where is your PyInstaller directory? ")
