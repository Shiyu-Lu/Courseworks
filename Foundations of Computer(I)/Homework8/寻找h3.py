import re
m = \
    r'\b[a-z1-9]\w{2}\b'
for x in  re.findall(m,"cdef<h3>abd</h3><h3>bcK</h3><h3>123</h3>KJM"):
    print (x)