#coding=utf-8
limit=28123
#limit=1000
AbundantList=[]
NonAbundantList=[]
test=[0]*(limit+1)
def isAbundantNumber(n):
	tsum=0
	for i in range(1,n/2+1):
		if n%i==0:
			tsum+=i
	if tsum>n:
		return True
	return False

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

print AbundantList
print NonAbundantList
print sum(NonAbundantList)
