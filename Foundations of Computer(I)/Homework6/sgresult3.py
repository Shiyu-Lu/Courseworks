'''

sgresult3.png		三国演义中出现频率前十的人名。必须是这十个名字。名字组成心形。心形图片可以用 love.png

'''

# 导入扩展库
import re # 正则表达式库
import collections # 词频统计库
import numpy as np # numpy数据处理库
import jieba # 结巴分词
import wordcloud # 词云展示库
from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
import os
from wordcloud import WordCloud, ImageColorGenerator
import pdb

# 读取文件
fn = open('三国演义utf8.txt',encoding='utf-8') # 打开文件
txt = fn.read() # 读出整个文件
fn.close() # 关闭文件

words = jieba.lcut(txt) #精确模式分词
items = []
excludes = ['将军','却说','荆州','二人','不可', '不能','如此','丞相','商议','如何','主公',
            '军士','左右','引兵','次日','军马','大喜','天下','东吴','于是','今日','不敢','魏兵','陛下']
for word in words:
    if len(word) == 1 or (word in excludes): continue
    elif word == "诸葛亮" or word == "孔明曰": word = "孔明"
    elif word == "关公" or word == "云长" or word == "关云长": word = "关羽"
    elif word == "玄德" or word == "玄德曰": word = "刘备"
    elif word == "孟德" or word == "操贼": word = "曹操" 
    items.append(word)

# 词频统计
word_counts = collections.Counter(items) # 对分词做词频统计
word_counts_top10 = word_counts.most_common(10) # 获取前10最高频的词

# 词频展示
font_path = 'SourceHanSerif/SourceHanSerifK-Light.otf'    # 加载显示的字体
back_coloring = imread('love.png')  # 要把词云放在什么图片里
wc = wordcloud.WordCloud(font_path=font_path, background_color="white", max_words=10, mask=back_coloring,
               max_font_size=100, random_state=42, width=316, height=97, margin=2,)

wc.generate_from_frequencies(word_counts) # 从字典生成词云
plt.figure()
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()