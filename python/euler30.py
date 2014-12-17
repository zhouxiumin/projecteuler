#coding=utf-8
n=4
resultlist=[]
for i in xrange(2,413343):
	llist=list(str(i))
	sum=0
	for j in llist:
		sum+=pow(int(j),n+1)
	if i==sum:
		resultlist.append(i)
print resultlist
sum=0
for i in resultlist:
	sum+=i
print sum
