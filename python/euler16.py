#coding=utf-8
llist=[]
for i in range(2,101):
	for j in range(2,101):
		temp=pow(i,j)
		if temp not in llist:
			llist.append(temp)
print len(llist)