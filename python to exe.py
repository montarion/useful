#imports
import os
from time import sleep


#pythonfile = input("what file do you want to make into an exe? ")
pythonfile = "anime-tracker.py"
#installdir = input("where is your PyInstaller directory? ")
installdir = "D:\downloads\PyInstalle\PyInstaller-3.2"
workdir = os.path.join(installdir, pythonfile[:-3])
exefile = os.path.join(workdir, "dist", pythonfile[:-3], pythonfile[:-3]+".exe" )

os.chdir(installdir)
#ls = os.popen("dir")
#(ls.read())
try:
    os.mkdir(workdir)
except:
    pass
os.chdir(workdir)



#check to see if things have been done---#


print("welcome!")
print("there are some things that you should do first..")
print("*add your python file to the 'python")
#pythonfile = input("what file do you want to make into an exe? ")
#installdir = input("where is your PyInstaller directory? ")
print(os.system("dir"))
check = os.path.isfile("check.txt")
print(check)
print("her i am")
ls = os.popen("dir")
print(ls.read())
os.chdir(installdir)
if check == True:
    print("The file " + pythonfile[:-3]+".exe" + " should already exist. Opening now..")
    sleep(2)
    print(exefile)
    os.system("explorer.exe /select," + exefile)
    exit()






print("initiating phase 2")
filedir = os.path.join(installdir, pythonfile)
print(workdir)
sleep(1)




print("working..")
os.system("python pyinstaller.py " + os.path.join(installdir, "python-files", pythonfile))


'''
    print("please remove the following directory manually:")
    print(" [dist] ")
    print("opening directory in question..")
    sleep(2)
    os.system("explorer.exe /select," + installdir)

'''


sleep(2)
print("done!")
print("opening output file..")
sleep(1)
os.system("explorer.exe /select," + exefile)

#---writing file for next use---#
finalcheck = os.path.isfile(exefile)
print(finalcheck)
if finalcheck == True:
    chdir = os.chdir(workdir)
    infile = open("check.txt", "w")
    infile.write("written")
    infile.close()
    print("done with writing")
print()
