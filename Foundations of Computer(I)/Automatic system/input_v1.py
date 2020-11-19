'''作业要求:
实现一个学生信息录入和查询系统

录入部分：
学生姓名，学号，Gpa，年龄，还有照片。学号不能重复。
照片通过文件对话框选取图片文件完成，要求支持.jpg
选了照片要能显示在界面上。然后点一个“提交”按钮，就将信息提交到数据库文件 students.db里面。如果提交的学生学号重复了，要给出提示

查询部分：
启动以后，显示一个列表框，包含所有学生的姓名。点一个学生的姓名，就在几个编辑框显示该学生的所有信息，包括学号等，还能显示照片。可以在编辑框里修改这些信息，点击照片，就能修改照片成别的文件，点一个“修改”按钮，则信息被更新。

录入部分和查询部分先分两个程序写
'''

import tkinter as tk 
import tkinter.messagebox 
import sqlite3

db = sqlite3.connect("/Users/rachel/PKU/通选课/文计实验班/Homework/大作业2/info.db") # 自动创建名为info的数据库
cur = db.cursor() # 获取光标
sql = '''CREATE TABLE if not exists students 
        (id integer primary key, name text, gpa real, age integer, picture blob)''' # 创建名为students的表
cur.execute(sql) # 执行SQL命令

def exe(mylist): # 插入学生信息
    for s in mylist:
        cur.execute('INSERT INTO students VALUES(?,?,?,?,?,?)',(s[0],s[1],s[2],s[3],s[4])

infolist = [] # 建一个list存学生信息
while True:
    s = input().split()
    id, name, gpa, age = int(s[0]),s[1],float(s[2]),int(s[3])
    infolist.append((id,name,gpa,age,'null'))
    
exe(infolist)

db.commit() #真正写入
cur.close() #关闭光标
db.close() #关闭数据库




 