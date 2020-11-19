import requests
import bs4
import re
import datetime

def getHTMLText(url):
        try:
                r = requests.get(url)
                return r.text 
        except:
                return ""

# 城市全列表
citylist = {'北京':'beijing','上海':'shanghai'} # 城市元素待添加

date_list = []
monthday = [0,31,28,31,30,31,30,31,31,30,31,30,31]

now_year = int(datetime.datetime.now().strftime('%Y')) # 获得目前的日期
now_month = int(datetime.datetime.now().strftime('%m'))
now_day = int(datetime.datetime.now().strftime('%d'))

# 给定年月日，生成标准格式的日期
def date(YYYY,MM,DD):
    d = 0
    if MM < 10:
        if DD <10:
            d = str(YYYY)+'0'+str(MM)+'0'+str(DD)
        elif DD >= 10:
            d = str(YYYY)+'0'+str(MM)+str(DD)
    else:
        if DD <10:
            d = str(YYYY)+str(MM)+'0'+str(DD)
        elif DD >= 10:
            d = str(YYYY)+str(MM)+str(DD)
    return d

# 完善date_list
def get_datelist(start_year,end_year,start_month,end_month,start_day,end_day)
    for YYYY in range(start_year,end_year+1): #先用2018和2019年的数据测试，之后再改
        for MM in range(start_month,end_month):
            for DD in range(start_day,end_day):
                date_list.append(date(YYYY,MM,DD))
        # if YYYY < now_year:
        #     for MM in range(1,13):
        #         for DD in range(1,monthday[MM]+1):
        #             date_list.append(date(YYYY,MM,DD))
        # elif YYYY == now_year:
        #     if now_month > 1:
        #         for MM in range(1,now_month-1):
        #             for DD in range(1,monthday[MM]+1):
        #                 date_list.append(date(YYYY,MM,DD))
        #         for MM in range(now_month,now_month+1):
        #             for DD in range(1,now_day+1):
        #                 date_list.append(date(YYYY,MM,DD))
        #     elif now_month == 1:
        #         for MM in range(now_month,now_month+1):
        #             for DD in range(1,now_day+1):
        #                 date_list.append(date(YYYY,MM,DD))         
# print (date_list) # 已经测试过了，date_list部分没有问题

# 定义模版代码


# 抓取每个城市的数据
for city in citylist:
    for date in date_list:
        # 打开某城市在YYYY-MM-DD这天的历史天气查询的源代码
        html1 = getHTMLText('http://www.tianqihoubao.com/lishi/'+citylist[city]+'/'+date+'.html')

