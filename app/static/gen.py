import os, math
from PIL import Image
from PIL import ImageDraw
import os
def turn(name):
    print(name)
    ima = Image.open("./save_file/"+name+".jpg").convert("RGBA")
    size = ima.size
    imb = Image.new('RGBA', (size[1], size[0]),(255,255,255,0))
    pima = ima.load()
    pimb = imb.load()
    for i in range(size[1]):
        for j in range(size[0]):
            pimb[i,j] = pima[j,i]
    imb.convert("RGB")
    imb.save("./save_file/"+name+".png")

def circle(name):
    print(name)
    ima = Image.open("./save_file/"+name+".jpg").convert("RGBA")
    size = ima.size
    # 因为是要圆形，所以需要正方形的图片
    r2 = min(size[0], size[1])
    if size[0] != size[1]:
        ima = ima.crop((0,0,r2, r2))


    imb = Image.new('RGBA', (r2, r2),(255,255,255,0))
    pima = ima.load()
    pimb = imb.load()
    r = float(r2/2) #圆心横坐标
    for i in range(r2):
        for j in range(r2):
            lx = abs(i-r+0.5) #到圆心距离的横坐标
            ly = abs(j-r+0.5)#到圆心距离的纵坐标
            l  = pow(lx,2) + pow(ly,2)
            if l <= pow(r, 2):
                pimb[i,j] = pima[i,j]
    imb = imb.resize((127, 127), Image.ANTIALIAS)
    imb.save("./people_png/"+name+".png")

if __name__ == '__main__':
    circle('韩_风')
    exit()
    for filename in os.listdir(r'./save_file'):
        if(os.path.isfile('./save_file/'+filename)):
            name=filename.split('.',1)[0]
            circle(name)

