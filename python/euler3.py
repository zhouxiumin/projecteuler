#coding=utf-8
import math
num=600851475143L
s=int(math.sqrt(num))+1
print s

primes=[2]
flag=False
for i in range(3,s,2):
	flag=True
	for j in primes:
		if i%j==0:
			flag=False
			break
	if flag:
		primes.append(i)

for i in primes:
	if num%i==0:
		print i
