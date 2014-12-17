#coding=utf-8
def dn(n):
	i=0
	tmp=n
	while True:
		k=(i+1)*9*10**i
		pre=tmp
		tmp-=k
		if tmp<=0:
			break
		i+=1
	c=pre/(i+1)
	yc=pre%(i+1)
	if yc==0:
		result=(10**i+c-1)%10
	else:
		result=int(list(str(10**i+c+1))[yc-1])
	return result


mul=1
for i in range(7):
	mul*=dn(10**i)
print mul