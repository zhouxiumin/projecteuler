#coding=utf-8
def gcd(m,n):
	if n==0:
		return m
	return gcd(n,m%n)

rfz=0
rfm=1
for fm in xrange(3,1000001):
	fz=int(fm*3/7)-1
	pre=fz
	while 7*fz<3*fm:
		if gcd(fz,fm)==1:
			pre=fz
		fz+=1
	if pre*rfm>rfz*fm:
		rfz=pre
		rfm=fm

print rfz,rfm
print "%d/%d"%(rfz,rfm)
