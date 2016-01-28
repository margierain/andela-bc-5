# for one start (i.e *args) args you mean that it's a tuple not a dict..
def my_sum(*args):
	total = 0
	for i in args:
		total += i
	return total

print "my sum:", my_sum(10,20)    
print "my_sum:", my_sum(10, 20,30,40,50)