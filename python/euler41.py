#coding=utf-8
from math import sqrt
def  isprime(n):
	if n==1:
		return False
	k=int(sqrt(n))+1
	for i in range(2,k):
		if n%i==0:
			return False
	return True

def perm(l):
	if len(l)<=1:
		return [l]
	r=[]
	for i in range(len(l)):
		s=l[:i]+l[i+1:]
		p=perm(s)
		for x in p:
			r.append(l[i:i+1]+x)
	return r

str='7654321'
for i in range(9):
	sub=str[i:9]
	l=perm(sub)
	flag=False
	for j in l:
		if isprime(int(j)):
			flag=True
			break
	if flag:
		print j
		break
