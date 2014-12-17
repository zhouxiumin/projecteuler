#coding=utf-8
import math
cach=[x*x for x in range(1,1000)]
res=[0]*1000
print cach
for i in range(1,1000):
	for j in range(1,1000):
		if i*i+j*j in cach:
			t=int(i+j+math.sqrt(i*i+j*j))
			if t<1000:
				res[t]+=1
max=0
result=1
for i in range(1,1000):
	if res[i]>max:
		result=i 
		max=res[i]

print res
print result
