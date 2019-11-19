import sys
from time import sleep
total = 342
i = 0


#print('do stuff')
def prog(count, total):
    percentage = count / total * 100
    percentage = round(percentage, 2)
    sys.stdout.write("progress: %d%%   \r"%(percentage))
    #sleep(0.2)
    #i += 1

prog(49, total)
sleep(2)
#print('moar')
prog(90, total)
sleep(2)
print("------\n\n\n")
def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()

while i < total:
    progress(i, total, "stuff")
    sleep(0.03)
    i +=1
