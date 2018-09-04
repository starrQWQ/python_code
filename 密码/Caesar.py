s=str.lower(raw_input("input:"))
i=1
l=[]
print s
for i in range(1,26):
	for j in range(len(s)):
		l.append(chr(97+(ord(s[j])+i)%97%26))
	print 'key'+'%d' %i
	print ''.join(l)
	l=[]
	i+=1