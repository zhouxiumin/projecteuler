#coding=utf-8
from math import sqrt
big=1e18
beg=int(sqrt(big))
end=int(sqrt(big*2))+1
s='1234567890'
for i in xrange(beg,end):
	if i%10!=0:
		continue
	ans=str(i*i)
	flag=True
	for j in range(10):
		if ans[2*j]!=s[j]:
			flag=False
			break
	if flag:
		print i,ans
		break

