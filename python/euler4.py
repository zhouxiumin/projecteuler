#coding=utf-8
def isPalindromeNumber(number):
	strlist=list(str(number))
	l=len(strlist)/2
	flag=True
	for i in range(l):
		if strlist[i]!=strlist[-i-1]:
			flag=False
			break
	return flag

max=0
for i in range(100,1000):
	for j in range(100,1000):
		temp=i*j
		if isPalindromeNumber(temp):
			if temp>max:
				max=temp;
print max