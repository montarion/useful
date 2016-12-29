#imports
import os
import subprocess

from time import sleep


#pythonfile = input("what file do you want to make into an exe? ")
pythonfile = "anime-tracker.py"
installdir = "D:\downloads\PyInstalle\PyInstaller-3.2"
workdir = os.path.join(installdir, pythonfile[:-3])
exefile = os.path.join(workdir, "dist", pythonfile[:-3], pythonfile[:-3]+".exe" )

os.chdir(installdir)
ls = os.popen("dir")
(ls.read())
try:
    os.mkdir(workdir)
except:
    pass
os.chdir(workdir)



#check to see if things have been done---#


print("welcome!")

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




ls = os.popen("dir")
(ls.read())

'''test = os.popen("dir")
print(test.read())'''
errormsg = "something went wrong, please contact your administrator."
'''try:
    os.chdir("python-file")
except:
    os.mkdir(installdir + "\\" + "python-file")
    print("couldn't create directory.")
    print(errormsg)
    pass'''

print("initiating phase 2")
filedir = os.path.join(installdir, pythonfile)
print(workdir)
sleep(1)
print("heyy")
os.system("dir")





try:
    step2 = os.popen("python pyinstaller.py " + installdir + "\python-files" + "\\" + pythonfile)

    print("working..")

except:
    print(errormsg)
    print("please remove the following directory manually:")
    print(" [dist] ")
    subprocess.Popen(r'explorer /select, "D:\downloads\PyInstalle\PyInstaller-3.2\anime-tracker\"')
    #print(step2.read())


sleep(2)
print("done!")
print("opening output file..")
sleep(1)
#os.system("explorer.exe /select," + exefile)

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
