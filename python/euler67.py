import re
line=100
fl=open('triangle.txt','r')
content=fl.read()
s=content
print s
llstr=re.split(r'\n',s)
print llstr
for i in range(len(llstr)):
	llstr[i]=[int(x) for x in re.split(r' ',llstr[i])]
print llstr
res=[[0]*line for i in range(line)]
res[0][0]=llstr[0][0]
print res
for i in range(1,line):
	for j in range(i+1):
		if j==0:
			res[i][j]=res[i-1][j]+llstr[i][j]
		elif j==i:
			res[i][j]=res[i-1][j-1]+llstr[i][j]
		else:
			res[i][j]=max(res[i-1][j]+llstr[i][j],res[i-1][j-1]+llstr[i][j])
print max(res[line-1])
