#coding=utf-8
n=1000
sum=0
for i in range(1,n):
	if i%3==0 or i%5==0:
#		print i
		sum+=i

print sum

x,y,z=1,2,3
print x,y,z

foo1=foo2=3.4
print foo1,foo2
print id(foo1)
print id(foo2)