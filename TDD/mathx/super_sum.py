def super_sum(*args):
	''' sum up the arguments
	'''
	total = 0

	for i in args:
		if isinstance(i, (list, tuple)):
			for arg in i:
				total += arg
		else:
			total += i



	return total

print super_sum([20, 40], [20, 30])

