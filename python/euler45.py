#coding=utf-8
from math import sqrt
def isTri(t):
	delta=1+8*t
	if int(sqrt(delta))**2==delta:
		return True
	return False

def isPen(p):
	delta=1+24*p
	t=int(sqrt(delta))
	if t**2==delta and (t+1)%6==0:
		return True		
	return False

n=143
while True:
	n+=1
	hn=n*(2*n-1)
	if isPen(hn) and isTri(hn):
		print n,hn
		break
