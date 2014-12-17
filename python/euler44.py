#coding=utf-8
import math
def pn(n):
	return n*(3*n-1)/2

def ispn(p):
	delta=1+24*p
	sq=int(math.sqrt(delta))
	if sq*sq!=delta:
		return False
	if (1+sq)%6==0:
		return True
	else:
		return False

i=1900
while True:
	d=pn(i)
	print i,d
	j=2
	flag=False
	while pn(j+1)-pn(j)<d:
		if ispn(d+pn(j)) and ispn(d+2*pn(j)):
			flag=True
			break
		j+=1

	if flag:
		break
	i+=1

print d