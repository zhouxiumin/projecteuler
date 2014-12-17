#coding=utf-8
fl=open('matrix.txt','r')
matrixSize=80
content=fl.read()
conlist=content.split('\n')

for i in range(len(conlist)):
	conlist[i]=[int(k) for k in conlist[i].split(',')]
print conlist
record=[[0]*matrixSize for i in range(matrixSize)]
#print record
total=0
for i in range(matrixSize):
	record[0][i]=total+conlist[0][i]
	total+=conlist[0][i]
total=0
for i in range(matrixSize):
	record[i][0]=total+conlist[i][0]
	total+=conlist[i][0]
for i in range(1,matrixSize):
	for j in range(1,matrixSize):
		record[i][j]=min(record[i-1][j],record[i][j-1])+conlist[i][j]
print record
print record[matrixSize-1][matrixSize-1]