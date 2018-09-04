tn=0
sn=[]
n=int(raw_input('n='))
a=int(raw_input('a='))
for i in range(n):
	tn+=a
	a*=10
	sn.append(tn)
	print tn
sn=reduce(lambda x,y:x+y,sn)
print 'the total is:%d'%sn