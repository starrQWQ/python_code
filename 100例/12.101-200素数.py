from math import sqrt
total=0
leap=1
for i in range(101,201):
	j=int(sqrt(i+1))
	for k in range(2,j+1):
		if i%k==0:
			leap=0
			break
	if leap==1:
		print '%-4d' % i
		total+=1
		if total%10==0:
			print ''
	leap=1

print 'the total is %d' %total