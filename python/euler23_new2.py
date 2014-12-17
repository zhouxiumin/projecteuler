#coding=utf-8
import math
limit=28123
#limit=1000
AbundantList=[]
NonAbundantList=[]
test=[0]*(limit+1)
def isAbundantNumber(n):
	tsum=1
	sq=int(math.sqrt(n))
	for i in range(2,sq+1):
		if n%i==0:
			if i!=n/i:
				tsum+=i+n/i
			else:
				tsum+=i
	if tsum>n:
		return True
	return False

#print isAbundantNumber(4)

for i in range(1,limit+1):
	if isAbundantNumber(i):
		AbundantList.append(i)

for i in AbundantList:
	for j in AbundantList:
		if i+j<=limit:
			test[i+j]=1
		else:
			break

for i in range(1,limit+1):
	if test[i]==0:
		NonAbundantList.append(i)

#print AbundantList
#print NonAbundantList
print sum(NonAbundantList)
