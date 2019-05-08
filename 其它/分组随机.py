#-*-coding:UTF-8 -*-
import random
names=["赫靖涛","周旭峰","罗泽宇","王强","邢航宁","张文博","张效林","费伊扬","杨李燕","夏昊晴"];
sections=["1、2","3、4","5","6","7","8","9","10","11","12"]
random.shuffle(names);
random.shuffle(sections);
for i in range(10):
	print names[i],"第%s节"%sections[i];
 