#coding=utf-8
import math
def perm(l):
	length=len(l)
	if(length<=1):
		return [l]
	r=[]
	for i in range(length):
		r.append(l[i:length]+l[0:i])
	return r

s=1000000
primes=[2]
flag=False
for i in xrange(3,s,2):
	flag=True
	k=int(math.sqrt(i))+1
	for j in primes:
		if i%j==0:
			flag=False
			break
		if k<j:
			break
	if flag:
		primes.append(i)

noprimes=[2]
for i in primes:
	flag=True
	for j in list(str(i)):
		if int(j)%2==0:
			flag=False
			break
	if flag:
		noprimes.append(i)

print noprimes
circularprimes=[]
err=[]
erro=[]
for i in noprimes:
	flag=True
	plist=perm(str(i))
	for stri in plist:
		if int(stri) not in primes:
			flag=False
			err.append(int(stri))
			erro.append(i)
			break
	if flag:
		circularprimes.append(i)

print erro
print err
print circularprimes
print len(circularprimes)