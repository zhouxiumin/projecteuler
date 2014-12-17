#coding=utf-8
res=[]
for i in range(10,99):
	i1=i/10
	i2=i%10
	if i%11==0:
		continue
	for j in range(10,i):
		j1=j/10
		j2=j%10
		if (j2==i1 and i2*j==i*j1) or (j1==i2 and i1*j==i*j2):
			res.append(str(j)+'/'+str(i))
print res