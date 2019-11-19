import keyboard, os

#root check
id = os.geteuid()

if id != 0:
   print("You must be root!")
   exit()


i = 1
print('press the enter button to go up 1')
while True:
    try:
        keyboard.wait('enter')
        print(i, flush=True)
        i += 1
    except KeyboardInterrupt:
        print("Pressed enter {} times!".format(i))
        exit() 
