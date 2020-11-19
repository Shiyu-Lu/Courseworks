from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os
import time
from time import strftime
import re

def needrotate(img): 
    up = img.getpixel((300,10))
    down = img.getpixel((300,-10))
    if up[2] < down[2]:
        img = img.transpose(Image.FLIP_TOP_BOTTOM)
        
    return img

def addtime(filepath):
    seconds = os.path.getctime(filepath)
    x = time.localtime(seconds)
    year = x[0]
    month = x[1]
    day = x[2]
    s = (str(year)+"年"+str(month)+"月"+str(day)+"日")
    return s

m = 0
def adddate(file, text, width, height,fontcolor):
    img = file
    drawObj = ImageDraw.Draw(img)
    font1 = ImageFont.truetype('System/Library/Fonts/SimHei.ttf',24) 
    drawObj.text((int(width*0.7),int(height*0.9)), text, fill = fontcolor, font = font1)  
    global m
    img.save('./HW12/graph/result/'+str(m)+'.png')
    m=m+1

lst = os.listdir("./HW12/graph/") #列出当前文件夹下所有文件和文件夹 
os.mkdir('./HW12/graph/result') # 创建result文件夹
for x in lst:
    if os.path.isfile("./HW12/graph/" + x): #如果x是文件 
        if x.lower().endswith(".jpg") or x.lower().endswith(".png"):
            img = Image.open("./HW12/graph/" + x) 
            width = img.size[0]
            height = img.size[1]

            # 让程序自动发现倒过来的照片
            img = needrotate(img) 

            # 识别右下角深浅，确定字体颜色
            points_total = int(0.01*width*height)
            brightness1 = 0
            for i in range(int(0.9*width),width):
                for j in range(int(0.9*height),height):
                    rd = img.getpixel((i,j)) 
                    r,g,b = rd[0],rd[1],rd[2]
                    brightness = (r/225*299 + g/255*587 + b/225*114)/1000
                    brightness1 += brightness/points_total
            if brightness1 > 0.5:
                fontcolor = 'black'
            else:
                fontcolor = 'white'
            
            # 加字
            adddate(img,addtime("./HW12/graph/" + x),width,height,fontcolor) 