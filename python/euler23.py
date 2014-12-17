#coding=utf-8
limit=28123
#limit=1000
AbundantList=[]
NonAbundantList=[]
def isAbundantNumber(n):
	tsum=0
	for i in range(1,n/2+1):
		if n%i==0:
			tsum+=i
	if tsum>n:
		return True
	return False

def isNonAbundantN(n):
	global AbundantList
	for i in AbundantList:
		for j in AbundantList:
			if i+j==n:
				return False
	return True

for i in range(1,limit+1):
	if isNonAbundantN(i):
		NonAbundantList.append(i)
	if isAbundantNumber(i):
		AbundantList.append(i)

print AbundantList
print NonAbundantList
print sum(NonAbundantList)
