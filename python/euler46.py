#coding=utf-8
import math

def isin(x,a):
	low=0
	high=len(a)-1
	while low<=high:
		mid=(low+high)//2
		if a[mid]==x:
			return True
		elif a[mid]>x:
			high=mid-1
		else:
			low=mid+1
	return False

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

n=7
while True:
	n=n+2
	if isin(n,primes):
		continue
	flag=True
	for i in primes:
		if i==2:
			continue
		t=n-i
		if t<0:
			flag=False
			break
		t/=2
		if int(math.sqrt(t))**2==t:
			break
	if not flag:
		break

print n