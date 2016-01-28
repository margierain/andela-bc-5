

# split() converts a varible to a list
names = "cate kevin stella beat chris".split()
count = 0
for i in range(20,25):
	print "I'm {0}, and I'm {1}y/o".format(names[count], i)
	# alternative method
	print "I'm %s, and I'm %s y/o" %(names[count], i) 
	count+=1


# range(start, end, steps)
for x in range(10,-1,-1):
	print x
