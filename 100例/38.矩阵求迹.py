l=[]
sum=0.0
n=int(raw_input('the dimension of the matrix:'))
for i in range(n):
	l.append([])
	for j in range(n):
		l[i].append(float(raw_input('input a number:')))
for i in range(n):
	sum+=l[i][i]
print sum
