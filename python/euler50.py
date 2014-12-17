#coding=utf-8
from math import sqrt
from math import log
primes=[2]
s=1000000
for i in xrange(3,s,2):
	flag=True
	for j in primes:
		t=int(sqrt(i))
		if j>t:
			break
		if i%j==0:
			flag=False
			break
	if flag:
		primes.append(i)

print len(primes)
print s/log(s)
tsum=0
res=[]
for i in primes:
	tsum+=i
	if tsum>primes[-1]:
		break
	if tsum%2!=0 and tsum in primes:
		res.append(tsum)
print res