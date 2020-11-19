'''

sgresult1.png		三国演义中的常见词汇分布在“三国"这两个隶书字上，出现频率高的词字体大

'''

# 导入扩展库
import re
import collections
import numpy as np 
import jieba 
import wordcloud
from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
import os
from wordcloud import WordCloud, ImageColorGenerator
import pdb

# 读取文件
f = open('三国演义utf8.txt',encoding='utf-8') # 打开文件
txt = f.read() # 读出整个文件
f.close() # 关闭文件

words = jieba.lcut(txt) #精确模式分词
items = []
for word in words:
    if len(word) == 1: #过滤掉长度为1的词 
        continue
    else:
        items.append(word)

# 词频统计
word_counts = collections.Counter(items) # 对分词做词频统计

# 词频展示
font_path = 'SourceHanSerif/SourceHanSerifK-Light.otf'    # 加载显示的字体
back_coloring = imread('font.jpg')  # 要把词云放在什么图片里（这里时放到三国这两个字里）
wc = wordcloud.WordCloud(font_path=font_path, background_color="white", max_words=2000, mask=back_coloring,
               max_font_size=100, random_state=42, width=316, height=97, margin=2,)

wc.generate_from_frequencies(word_counts) # 从字典生成词云
plt.figure()
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()