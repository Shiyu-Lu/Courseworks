import re
import requests

def getHTMLText(url):
        try:
                r = requests.get(url)
                return r.text 
        except:
                return ""

f = open('words.txt',encoding='utf-8') 
file = f.read()
txt = re.split("\r|\t|\n",file)
f.close()

words = []
tem_word = '\$\S'
tem_synoids = 'id=\"synoid.*</span></a></div></div></div></div></div>'
tem_synoid = '\"p1\-4\"\>.*?</span'
tem_imgs = 'class="img_area.*?/></a></div><div'
tem_img = 'src=.*'

for i in txt:
        if re.match(tem_word,i):
                words.append(i)

for word in words:
        html = getHTMLText('https://cn.bing.com/dict/search?q='+word)
        try:
                sen = re.findall(tem_synoids,html)
                synoids = re.findall(tem_synoid,sen[0])
                f = open('./tmp/result.txt',"a",encoding='utf-8')
                f.write(word+'\n')
                for synoid in synoids:
                        s = re.split('>|<',synoid)
                        f.write(s[1]+'\n')
                f.close()
        except:
                pass
        try:
                sen2 = re.findall(tem_imgs,html)
                img = re.findall(tem_img,sen2[0])
                href = re.split('"',img[0])
                r = requests.get(href[1],stream=True)
                rw = word.split('$')
                f = open('./tmp/{0}{1}'.format(rw[1],'.png'),'wb')
                for chunk in r.iter_content():
                        f.write(chunk)
                f.close()
        except:
                pass