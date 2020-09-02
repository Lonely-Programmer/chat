from PIL import Image

def makeHead(srcImg):
    tx = Image.open(srcImg).resize((103,103)).convert("RGBA")
    mb = Image.open('src/tx/mb.png')
    mb.paste(tx, mask=mb)
    return mb

def drawHead(bgImg,startTop,who):
    bg=Image.open(bgImg)
    if who=="Me":
        startLeft=946
        srcImg="src/tx/M.png"
    else:
        startLeft=26
        srcImg="src/tx/U.png"
    rd=makeHead(srcImg).convert("RGBA")
    r,g,b,a = rd.split()
    bg.paste(rd,(startLeft,startTop,startLeft+103,startTop+103),mask=a)
    bg.save("bgEnd.png")
