#coding=utf-8
fl=open('names.txt','r')
content=fl.read()
conlist=content.split(',')
conlist.sort()
conlist=[i[1:-1] for i in conlist]
print conlist
tsum=0
for i in range(len(conlist)):
	tlist=[ord(j)-ord('A')+1 for j in list(conlist[i])]
	ss=sum(tlist)
	tsum+=ss*(i+1)
print tsum