import hashlib,sys
fp=open(sys.argv[1],'rb');
file=fp.read();

def option():
	print("1:md5\
		  \n2:sha-1\
		  \n3:sha-256\
		  \n4:sha-512\
		  \nquit to exit.")
	opt=raw_input("choose:");
	return opt;

opt=option();
while(opt!="quit"):
	print '*'*50;

	if (opt=='1'):
		print(hashlib.md5(file).hexdigest());
	elif (opt=='2'):
		print(hashlib.sha1(file).hexdigest());
	elif(opt=='3'):
		print(hashlib.sha256(file).hexdigest());
	elif(opt=='4'):
		print(hashlib.sha512(file).hexdigest());
	else:
		print("erorr.");
	print '*'*50;
	opt=option();
fp.close();


