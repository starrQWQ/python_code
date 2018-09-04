

list={};
for i in range(26):
	subList=[];
	for j in range(26):
		subList.append(chr(97+(i+j)%26));
	list[chr(97+i)]=subList;

print '   ',
for i in range(97,97+26):
	print chr(i)+'|',
for key in range(97,97+26):
	
	print ''
	print chr(key)+':|',
	for j in list[chr(key)]:
		print j+'|',
	print ''


def e(key,m):  
    c=[];
    key_len=len(key);
    for i in range(len(m)):
    	index_1=key[i%key_len];
    	c.append(list[index_1][ord(m[i])-97])
    ciphertext=''.join(c)
    print "ciphertext: "+ciphertext
    return ciphertext

def d(key,c):
	m=[];
	key_len=len(key);
	for i in range(len(c)):
		index_1=key[i%key_len];
		index_2=list[index_1].index(c[i])
		m.append(chr(97+index_2))
	plaintext=''.join(m)
	print "plaintext:"+plaintext;
	return plaintext

def main():
	opt=raw_input("1.encrypt\n2.decrypt\n3.quit\n");
	while(1):
		if(opt=='1'):
			key=raw_input("input the key:").lower();
			plaintext=raw_input("input the plaintext:");
			ciphertext=e(key,plaintext);
		elif(opt=='2'):
			key=raw_input("input the key:").lower();
			ciphertext=raw_input("input the ciphertext:");
			d(key,ciphertext)
		elif(opt=='3'):
			exit(0);
		opt=raw_input("1.encrypt\n2.decrypt\n3.quit\n");
		
	


if __name__ == '__main__':
	main()