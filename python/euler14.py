#coding=utf-8
def collatz(n):
	count=1
	while n!=1:
		n = n>>1 if (n&0x01==0) else (3*n+1)
		count+=1
	return count
maxnum=0
for i in xrange(1,1000000):
	temp=collatz(i)
	if maxnum<temp:
		maxnum=temp
		result=i
print result,maxnum