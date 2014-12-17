#coding=utf-8
k=1000
sum=0L
m=pow(10,10)
for i in range(1,k):
	sum+=pow(i,i,m)
sum=sum%m
print sum