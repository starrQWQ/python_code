tour=[]
hei=100.0
time=10
for i in range(1,time+1):
	if i==1:
		tour.append(hei)
	else:
		tour.append(2*hei)
	hei/=2
print 'total:%f'% sum(tour)
print '10th height£º%f' % hei
