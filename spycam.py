# Gets the files out of your spycam for infite recording(as long as you have power of course)
# And then moves it to and sftp server of choice
import shutil, os

campath = "/media/camera/VIDEO/"
storepath = "/home/pi/Downloads/"
files = os.listdir(campath)
filesize = []
filecheck = []
def check(filesize):
    speed = 4.5
    time = filesize/ speed / 60
    if time<5:
        return 0
    else:
        return 1    #1 means too big

for i in range(0, len(files)):
    filesize.append(int(os.path.getsize(campath+files[i])))
    totalsize = sum(filesize)
    finalsize = totalsize/1048000
    filecheck.append(check(finalsize))
biggest = (filecheck.index(1))-1
filelist = ','.join(files[:biggest])
print(filelist)
storagecheck = os.popen("df -hlP . | awk 'int($5)>1{print $4}'").read()
free_space = (int(storagecheck[:-4])*1000)              #from gb to mb
print(free_space)
writesize = int(sum(filesize[:biggest])/1000000)        #from b to mb
print(writesize)
if free_space > writesize:
    ("mv " +campath + "{"+ filelist + "} "+ storepath)
else:
    print("not enough storage to write to "+ str(storepath) + "!!\nOnly " +\
           str(free_space) + "MB left, while trying to write " + str(writesize) + "MB..")

