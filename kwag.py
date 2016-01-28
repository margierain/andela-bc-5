# kwags are used as dictionaries
def output(name, **kwags):
	print  "name:" , name
	for i in kwags.keys():
		print i, ":", kwags[i]

output('Angela', age=21, gender = 'f', loc = 'Nai')
