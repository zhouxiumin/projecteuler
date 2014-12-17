#coding=utf-8
def ispal(l):
	length=len(l)
	for i in range(0,length/2):
		if l[i]!=l[length-1-i]:
			return False
	return True

def dectobin(n):
	rl=[]
	while n!=0:
		rl.append(n%2)
		n/=2
	rl.reverse()
	return rl

tsum=0
resl=[]
for i in range(1,1000000):
	if ispal(str(i)) and ispal(dectobin(i)):
		tsum+=i
		resl.append(i)

print tsum
print resl	