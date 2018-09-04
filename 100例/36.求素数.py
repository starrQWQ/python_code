from math import sqrt
lower=int(input('the lower number:'))
upper=int(input('the upper number:'))
for num in range(lower,upper+1):
	for i in range (2,int(sqrt(num))+1):
		if num%i==0:
		    break			
	else:
		print num
