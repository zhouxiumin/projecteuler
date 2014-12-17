#coding=utf-8
def perm(l):
	if(len(l)<=1):
		return [l]
	r=[]
	for i in range(len(l)):
		s=l[:i]+l[i+1:]
		p=perm(s)
		for x in p:
			r.append(l[i:i+1]+x)
	return r

l='0123456789'
r=perm(l)
results=[]
for i in r:
	if r[0]=='0':
		continue
	elif int(i[1:4])%2!=0:
		continue
	elif int(i[2:5])%3!=0:
		continue
	elif int(i[3:6])%5!=0:
		continue
	elif int(i[4:7])%7!=0:
		continue
	elif int(i[5:8])%11!=0:
		continue
	elif int(i[6:9])%13!=0:
		continue
	elif int(i[7:10])%17!=0:
		continue
	else:
		results.append(int(i))
res=sum(results)
print results
print res

