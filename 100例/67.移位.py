def exchange(num,m):
	a=[]
	for i in range(m):
		a.append(num[-m])
		m-=1
	return a
	



if __name__ == '__main__':
    n = int(raw_input(' n:\n'))
    m = int(raw_input(' m:\n'))

    num=[]
    for i in range(n):
    	num.append(int(raw_input('input:')))
    a=exchange(num,m)
    print a
    for i in range(len(num)-m):
    	num[-i-1]=num[-i-1-m]
    for i in range(m):
    	num[i]=a[i]
    print num