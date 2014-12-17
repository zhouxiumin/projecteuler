#coding=utf-8
lmax=0
for i in range(1,100):
	for j in range(1,100):
		s=sum([int(x) for x in str(i**j)])
		if lmax<s:
			lmax=s

print lmax