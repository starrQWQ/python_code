# coding:utf-8

from __future__ import print_function
import sys
a=raw_input("input:")
for i in range(len(a)):
	print('&#'+str(ord(a[i])),end='')
print('')
for i in range(len(a)):
	sys.stdout.write('&#'+str(ord(a[i])))