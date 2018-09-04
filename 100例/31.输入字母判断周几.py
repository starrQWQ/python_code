letter=raw_input("input:")
if letter=='m' or letter=='M':
	print 'Monday'
if letter=='w' or letter=='W':
	print 'Wednesday'
if letter=='f' or letter=='F':
	print 'Friday'
if letter=='t' or letter=='T':
	letter=raw_input('input the second letter:')
	if letter=='u':
		print 'Tuesday'
	elif letter=='h':
		print 'Thursday'
if letter=='s' or letter=='S':
	letter=raw_input('input the second letter:')
	if letter=='a':
		print 'Saturday'
	else:
		print 'Sunday'