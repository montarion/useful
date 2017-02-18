
encoding = {'a': '1', 'b' : '11', 'c':'111', 'd':'2', 'e':'22', 'f':'222', 'g':'3', 'h':'33', 'i':'333', 'j':'4',
                  'k':'44', 'l':'444', 'm':'5', 'n':'55', 'o':'555', 'p':'6', 'q':'66', 'r':'666', 's':'7', 't':'77',
                  'u':'777', 'v':'8', 'w':'88', 'x':'888', 'y':'9', 'z':'99', ' ':'999', '.':'12', ',':'13', '!':'14'}

decoding = {'1': 'a', '11' : 'b', '111':'c', '2':'d', '22':'e', '222':'f', '3':'g', '33':'h', '333':'i', '4':'j',
                  '44':'k', '444':'l', '5':'m', '55':'n', '555':'o', '6':'p', '66':'q', '666':'r', '7':'s', '77':'t',
                  '777':'u', '8':'v', '88':'w', '888':'x', '9':'y', '99':'z', '999':' ', '12':'.', '13':',', '14':'!'}



def encode():
    sentence = input("Type the senctence to encode. ")
    test = sentence.lower()
    i = 0
    notalist = []
    while i < len(test):
        test2 = encoding[test[i]]
        notalist.append(str(test2))

        i = i + 1
    print("Your encoded sentence is: ")
    ugh = '-'.join(notalist)
    print(ugh)

def decode():
    sentence = input("Type the characters to decode. ")
    i = 0
    test = sentence.split('-')
    notalist = []
    while i < len(test):
        test2 = decoding[test[i]]
        notalist.append(str(test2))
        i += 1

    final = ''.join(notalist)
    print("Your decoded sentence is: '" + final + "'")



while True:
    option = input('What do you want to do? ')
    if option.lower() in ('encode', 'encrypt', '1'):

        encode()
    elif option.lower() in ('decode', 'decrypt', '2'):
        decode()
    else:
        print('Please answer with either encode, or decode. ')


