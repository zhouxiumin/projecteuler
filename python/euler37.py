#coding=utf-8
from math import sqrt
l=[1,3,5,7,9]
TruncatablePrimes=[23]
def isprime(n):
	if n==1:
		return False
	k=int(sqrt(n))+1
	for i in range(2,k):
		if n%i==0:
			return False
	return True

def istp(n):
	tmp=n/10
	while tmp!=0:
		if not isprime(tmp):
			return False
		tmp=tmp/10
	return True


def fn(n):
	global l,TruncatablePrimes
	for i in l:
		tmp=int(str(i)+str(n))
		if isprime(tmp):
			fn(tmp)
			if istp(tmp):
				TruncatablePrimes.append(tmp)

fn(3)
fn(7)
print TruncatablePrimes
print sum(TruncatablePrimes)