#coding=utf-8
def f(x,y):
	if x<=0 or y<=0:
		return 1
	return f(x-1,y)+f(x,y-1)

rows=21

fn=[[-1]*rows]*rows
for i in range(rows):
	fn[i][0]=1
for i in range(rows):
	fn[0][i]=1
for i in range(1,rows):
	for j in range(1,rows):
		fn[i][j]=fn[i-1][j]+fn[i][j-1]

print fn
print fn[20][20]