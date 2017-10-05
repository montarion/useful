import keyboard
i = 1
print('press the escape button to go up 1')
while True:
    keyboard.wait('esc')
    print(i)
    i += 1

