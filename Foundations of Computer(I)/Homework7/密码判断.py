import re

m = '[A-Za-z](\d|\-|\_|[a-zA-Z]){7,}$' # 记住match何时返回True，这里应用$结尾

while True:
    try:
        s = input()
        if re.match(m,s) != None:
            print("yes")
        else:
            print("no")
    except:
        break