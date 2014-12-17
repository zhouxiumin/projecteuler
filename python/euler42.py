#coding=utf-8
from math import sqrt 
def isTriangleWords(l):
	tsum=0
	for i in l:
		tsum+=ord(i)-ord('A')+1
	delta=1+8*tsum
	t=int(sqrt(delta))
	if t*t==delta:
		return True
	return False

fl=open('words.txt','r')
content=fl.read()
conlist=content.split(',')
conlist=[i[1:-1] for i in conlist]
print conlist
count=0
for i in conlist:
	if isTriangleWords(i):
		count+=1
print count
fl.close()