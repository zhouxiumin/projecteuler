#coding=utf-8
import re
s='''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''
llstr=re.split(r'\n',s)
for i in range(len(llstr)):
	llstr[i]=[int(x) for x in re.split(r' ',llstr[i])]
print llstr
res=[[0]*15 for i in range(15)]
res[0][0]=llstr[0][0]
print res
for i in range(1,15):
	for j in range(i+1):
		if j==0:
			res[i][j]=res[i-1][j]+llstr[i][j]
		elif j==i:
			res[i][j]=res[i-1][j-1]+llstr[i][j]
		else:
			res[i][j]=max(res[i-1][j]+llstr[i][j],res[i-1][j-1]+llstr[i][j])
print max(res[14])