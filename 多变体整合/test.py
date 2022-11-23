import os

pat = os.getcwd()



a = 2
b = a**4
tmp = []
tmp.append(a)
tmp.append(b)
c = []
c.append(tmp)
c.append(tmp)

fp = open(pat+'\\tmp.txt',a)