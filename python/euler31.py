#coding=utf-8
array=[[-1]*201]*201
def fn(n,m):
	if m>n:
		return fn(n,n)
	if m==n:
		return 1
	if m==1 or n==1:
		return 1
	global array
	if array[n][m]!=-1:
		return array[n][m]
	else:
		t=n-m
		l=[1,2,5,10,20,50,100,200]
		ll=[x for x in l if x<=m]
		s=0
		for j in ll:
			s+=fn(t,j)
		array[n][m]=s
		return s

print fn(200,200)
