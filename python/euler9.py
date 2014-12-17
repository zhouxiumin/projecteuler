#coding=utf-8
for a in range(1,1000):
	for b in range(1,1000):
		c=1000-a-b
		if c<0:
			break
		if a**2+b**2==c**2:
			print a*b*c
			break