#coding=utf-8
fz=1
fm=2
count=0
for i in range(2,1001):
	temp=fm
	fm=fm*2+fz
	fz=temp
	rfz=fm+fz
	if len(str(rfz))>len(str(fm)):
		count+=1
print count