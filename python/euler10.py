#coding=utf-8
import math
s=2000000
primes=[2]
flag=False
for i in xrange(3,s,2):
	flag=True
	k=int(math.sqrt(i))+1
	for j in primes:
		if i%j==0:
			flag=False
			break
		if k<j:
			break
	if flag:
		primes.append(i)
sum=0
for i in primes:
	sum+=i
print sum
#print primes