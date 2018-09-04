# encoding:utf-8
import urllib
import base64

def option():
	print("1.urlencode\
	\n2.urldecode\
	\n3.base64 encode\
	\n4.base64 decode");

	print("input 'quit' to quit");
	opt=raw_input("mode:");
	
	return opt;

opt=option();

while(opt!='quit'):
	s=raw_input("the string:");

	if (opt=='1'):
		print(urllib.quote(s));
	elif (opt=='2'):
		print(urllib.unquote(s));
	elif(opt=='3'):
		print(base64.b64encode(s));
	elif(opt=='4'):
		a=base64.b64decode(s);
		print(a+'\n'+str(len(a)));

	opt=option();

