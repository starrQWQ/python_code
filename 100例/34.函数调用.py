def hello():
	print 'hello'
def three_hello():
	for i in range(3):
		hello()
if __name__ == '__main__':
	three_hello()