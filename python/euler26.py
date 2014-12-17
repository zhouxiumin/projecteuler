#coding=utf-8

def onedigit(n):
	reslist=[]
	rlist=[]
	fz=1
	while True:
		if fz==n:
			reslist.append(1)
			rlist.append(0)
			return 0
		else:
			reslist.append(fz/n)
			if fz%n in rlist:
				clist=reslist[rlist.index(fz%n)+1:]
				return len(clist)
			else:
				rlist.append(fz%n)
			fz=(fz%n)*10

maxlength=0
num=0
for i in range(1,1000):
	length=onedigit(i)
	if length>maxlength:
		maxlength=length
		num=i
print 'answer',num,maxlength