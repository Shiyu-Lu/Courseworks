'''

写三个程序，生成三幅云词图:
 
sgresult1.png		三国演义中的常见词汇分布在“三国"这两个隶书字上，出现频率高的词字体大
sgresult2.png		三国演义中出现频率前十的人名。必须是这十个名字。图片长宽比是2:1
sgresult3.png		三国演义中出现频率前十的人名。必须是这十个名字。名字组成心形。心形图片可以用 love.png

'''

# 导入扩展库
import re # 正则表达式库
import collections # 词频统计库
import numpy as np # numpy数据处理库
import jieba # 结巴分词
import wordcloud # 词云展示库


# 读取文件
fn = open('三国演义utf8.txt') # 打开文件
string_data = fn.read() # 读出整个文件
fn.close() # 关闭文件

# 文本预处理
pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"') # 定义正则表达式匹配模式
string_data = re.sub(pattern, '', string_data) # 将符合模式的字符去除

# 文本分词
seg_list_exact = jieba.cut(string_data, cut_all = False) # 精确模式分词
object_list = []
# remove_words = [u'的', u'，',u'和', u'是', u'随着', u'对于', u'对',u'等',u'能',u'都',u'。',u' ',u'、',u'中',u'在',u'了',
#                 u'通常',u'如果',u'我们',u'需要'] # 自定义去除词库

for word in seg_list_exact: # 循环读出每个分词
    if word not in remove_words: # 如果不在去除词库中
        object_list.append(word) # 分词追加到列表

# 词频统计
word_counts = collections.Counter(object_list) # 对分词做词频统计
word_counts_top10 = word_counts.most_common(10) # 获取前10最高频的词
# print (word_counts_top10) # 输出检查

# 词频展示
mask = np.array(Image.open('love.jpg')) # 定义词频背景
wc = wordcloud.WordCloud(font_path=font_path, background_color="white", max_words=10,
               max_font_size=100, random_state=42, width=500, height=250, margin=2,)
)

wc.generate_from_frequencies(word_counts) # 从字典生成词云
image_colors = wordcloud.ImageColorGenerator(mask) # 从背景图建立颜色方案
wc.recolor(color_func=image_colors) # 将词云颜色设置为背景图方案
plt.imshow(wc) # 显示词云
plt.axis('off') # 关闭坐标轴
plt.show() # 显示图像