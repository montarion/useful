import subprocess
def drives():

        # Disconnect anything on M
        #doesn't work, ignore.
        #subprocess.call(r'net use m: /del', shell=False)
        print('mapping network drive..')

        # Connect to shared drive, use var driveletter
        # syntax if not using var driveletter: r'net use c(yes, lowercase): \\host\folder /user:username password
        subprocess.run(r'net use '+driveletter+': \\\GREYWOLF\storagedrive ')





driveletter = input('what drive do you want to use?')
drives()
print('using drive: ',driveletter)
#syntax for drive is r'z:\'
drive = str("r'" + driveletter + ":\'")

#choose filename
firstfilename = input('what is the name of the new file?')
#gives proper txt extension if it's not there yet
if '.' not in firstfilename :
    extension = '.txt'

    filename = str(firstfilename + '.txt')


location = drive + filename
infile = open(location,'w')
filedata = input('what text do you want in ' + filename + '? ')
infile.write(filedata)
infile.close()


driveletter2 = driveletter.upper()
drivelocation = driveletter2 + r':/' + filename
print(drivelocation)
infile = open(drivelocation)
outfile = infile.read()
print('the file', filename, 'contains')
print(outfile)

