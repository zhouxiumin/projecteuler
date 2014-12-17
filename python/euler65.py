#coding=utf-8
def generatList(n):
	llist=[]
	for i in range(n):
		t=1
		if i%3==1:
			t=2*(i/3+1)
		llist.append(t)
	return llist[::-1]

def generatitem(n):
	fz=0
	fm=1
	llist=generatList(n)
	for i in llist:
		temp=fm
		fm=fz+i*fm
		fz=temp
	return (fz+2*fm,fm)

fz=[int(x) for x in list(str(generatitem(99)[0]))]
print sum(fz)

