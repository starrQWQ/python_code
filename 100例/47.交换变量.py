def exchange(a,b):
	a,b=b,a
	return (a,b)

if __name__ == '__main__':
	a=1
	b=2
	print 'a=%d b=%d' % (a,b)
	a,b=exchange(a,b)
	print 'a=%d b=%d' % (a,b)
