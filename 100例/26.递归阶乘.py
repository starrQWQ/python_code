def mul(n):
	if n==0:
		return 1
	else:
		return n*mul(n-1)

n=int(raw_input('input an integer:'))
print mul(n)