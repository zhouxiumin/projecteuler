#coding=utf-8
limit=10000000
#limit=1000
count=0
res=[0]*601
for i in xrange(1,601):
	t=i
	while t!=1 and t!=89:
		tsum=0
		while t!=0:
			tsum+=(t%10)**2
			t/=10
		t=tsum
	res[i]=t

print res

for i in xrange(1,limit):
	t=i
	tsum=0
	while t!=0:
		tsum+=(t%10)**2
		t/=10
	if res[tsum]==89:
		count+=1
print count
