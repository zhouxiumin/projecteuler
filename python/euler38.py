#coding=utf-8
dig='123456789'

result=[]
results=[]
for i in range(5000,9999):
	tmp=str(i)+str(i*2)
	flag=True
	for j in dig:
		if j not in tmp:
			flag=False
	if flag:
		result.append(i)
		results.append(int(tmp))

for i in range(100,333):
	tmp=str(i)+str(i*2)+str(i*3)
	flag=True
	for j in dig:
		if j not in tmp or len(tmp)!=9:
			flag=False
			break
	if flag:
		result.append(i)
		results.append(int(tmp))

for i in range(10,34):
	tmp=str(i)+str(i*2)+str(i*3)+str(i*4)
	flag=True
	for j in dig:
		if j not in tmp or len(tmp)!=9:
			flag=False
			break
	if flag:
		result.append(i)
		results.append(int(tmp))

for i in range(1,10):
	tmp=str(i)+str(i*2)+str(i*3)+str(i*4)+str(i*5)
	flag=True
	for j in dig:
		if j not in tmp or len(tmp)!=9:
			flag=False
			break
	if flag:
		result.append(i)
		results.append(int(tmp))
print result
print results
print max(results)