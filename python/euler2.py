#coding=utf-8
sum=0
MAX=4000000
a=0
b=1
while True:
	c=a+b
	if c>MAX:
		break
	if c%2==0:
		sum+=c
	a=b
	b=c

print sum