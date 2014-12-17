#coding=utf-8
from math import sqrt
def isprime(n):
	if n<=1:
		return False
	t=int(sqrt(n))+1
	for i in range(2,t):
		if n%i==0:
			return False
	return True

def cot(a,b):
	n=0
	while True:
		if not isprime(n*n+a*n+b):
			break;
		n+=1
	return n

maxn=0
a=0
b=0
for i in range(-999,1000):
	for j in range(-999,1000):
		t=cot(i,j)
		if t>maxn:
			maxn=t
			a=i
			b=j

print a*b
print maxn
