def add(x,y):
	return x + y

y = lambda x , y: x + y
print y(10,2)
# without lambda
def make_incrementer(n):
	def inc(x):
		return x + n

	return inc
	# with lambda
def make_inc_lambda(n):
	return lambda x: x +n



z = make_incrementer(10)	