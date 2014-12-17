#coding=utf-8
cach=[1]*10
for i in range(1,10):
	cach[i]=i*cach[i-1]

end=int(3e6)
results=[]
for i in range(3,end):
	llist=list(str(i))
	s=0
	for j in llist:
		s+=cach[int(j)]
	if s==i:
		results.append(i)

result=sum(results)
print results
print result