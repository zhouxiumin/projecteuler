#coding=utf-8
def isleapyear(year):
	if (year%4==0 and year%100!=0) or year%400==0:
		return 1
	return 0

month=[31,28,31,30,31,30,31,31,30,31,30,31]

days=2
count=0
for i in range(1901,2001):
	month[1]=28+isleapyear(i)
	for j in range(12):
		days+=month[j]
		if days%7==0:
			count+=1

print 'result',count