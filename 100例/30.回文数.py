n=int(raw_input('intput an integer:'))
x=str(n)
flag=True
for i in range(len(x)):
	if x[i]!=x[-i-1]:
		flag=False
		break
if flag:
	print 'yes'
else:
	print 'no'