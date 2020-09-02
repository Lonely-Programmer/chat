from txtDialog import Chat
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import time

def generate():
    ch = 32
    with open('input.txt', 'r', encoding = 'utf-8') as f:
        for line in f:
            tmp = line.split('\t')
            if len(tmp) < 2:
                continue
            if ch == 32:
                src = 'bgSrc.png'
            else:
                src = 'bgEnd.png'
            if tmp[0] == 'L':
                name = 'U'
            elif tmp[0] == 'R':
                name = 'Me'
            else:
                print('ERROR!')
            msg = tmp[1]
            if msg[-1] == '\n':
                msg = msg[0:-1]
            ch = Chat(src,msg,ch+32,name)

    pic = Image.open('bgEnd.png')
    pic = pic.crop((0, 0, 1072, ch+64))
    pic.save('bgEnd.png')

def show():
    pic = mpimg.imread('bgEnd.png')
    plt.imshow(pic)
    plt.axis('off')
    plt.show()

def main():
    print('Generating... Please wait for a few seconds.')
    t = time.time()
    generate()
    print('Conplete! Output to [bgEnd.png]')
    print('Time:',round(time.time() - t,2),'s')
    show()

main()
