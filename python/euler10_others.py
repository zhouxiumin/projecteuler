#coding=utf-8
MAX_NUM = 2000000

isPrime = [1] *MAX_NUM
isPrime[0] = 0
isPrime[1] = 0
prime = 2

x = 2
while (x* 2) <= (MAX_NUM - 1) :
    isPrime[x*2] = 0
    x += 1

y = 3

while y <=  (MAX_NUM - 1):
    if (isPrime[y]):
        prime += y
        z = 2
        while (z*y) <= (MAX_NUM - 1):
            isPrime[z*y] = 0
            z += 1
    y += 2

print(prime)