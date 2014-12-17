#coding=utf-8
def gcd(a,b):
	if b==0:
		return a
	else:
		return gcd(b,a%b)

def lcm(a,b):
	return (a/gcd(a,b))*b

begin=1
end=20
mul=1
for i in xrange(begin,end+1):
	mul=lcm(mul,i)

print mul