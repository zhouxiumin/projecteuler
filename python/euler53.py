#coding=utf-8
def comb(n):
	res=[1]*(n+1)
	for i in range(1,n/2+1):
		res[i]=(n-i+1)*res[i-1]/i
	for i in range(n/2+1,n+1):
		res[i]=res[n-i]
	return res
print comb(5)
limit=1000000
count=0
for i in range(1,101):
	llist=comb(i)
	for j in llist:
		if j>limit:
			count+=1
print count
