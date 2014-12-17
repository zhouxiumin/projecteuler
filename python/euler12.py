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

dic={}
num=0
i=1
while num<=500:
	n=i*(i+1)/2
	dic.clear()
	result=n
	while n!=1:
		flag=True
		k=int(math.sqrt(n))+1
		for j in primes:
			if n%j==0:
				flag=False
				if dic.has_key(j):
					dic[j]+=1
				else:
					dic[j]=1
				n=n/j
				break
			if k<j:
				break
		if flag:
			if dic.has_key(n):
				dic[n]+=1
			else:
				dic[n]=1
			n=n/n
	num=1
	for j in dic:
		num*=dic[j]+1
	i+=1
print result
