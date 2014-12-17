#coding=utf-8
def d(n):
	sum=0
	for i in range(1,n/2+1):
		if n%i==0:
			sum+=i
	return sum
llist=[]
for i in range(100,10001):
	j=d(i)
	k=d(j)
	if i>j and i==k:
		llist.append(i)
		llist.append(j)
print llist
sumnum=0
for i in llist:
	sumnum+=i
print sumnum