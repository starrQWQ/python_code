def reduceNum(n):
	print '{}='.format(n),
	if n in [1]:
		print '{}'.format(n)
	while n not in [1]:
		for index in xrange(2,n+1):
			if n%index==0:
				n/=index
				if n==1:
					print index
				else:
					print '{}*'.format(index), 
				break
if __name__ == '__main__':
	n=int(raw_input('input an integer:'))
	reduceNum(n)