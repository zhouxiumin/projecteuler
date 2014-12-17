#coding=utf-8
def isPal(n):
	s=str(n)
	for i in range(len(s)/2):
		if s[i]!=s[len(s)-1-i]:
			return False
	return True

def rev(n):
	s=0
	t=n
	while t!=0:
		k=t%10
		s=10*s+k
		t/=10
	return s

def isLy(n):
	count=1
	t=n
	while count<=50:
		t=t+rev(t)
		if isPal(t):
			return False
		count+=1
	return True

count=0
for x in xrange(1,10000):
	if isLy(x):
		count+=1
print count