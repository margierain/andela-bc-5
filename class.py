class Vehicle(object):
	def __init__(self,**kwags):
# set a default value if the user doen't write it.		
		if kwags is not None:
		self.color = kwags.set('color', ' ')

def __init__(self, door, **kwags):
	    self.door = door
        for k, v in kwags.items():
        	setattr(self,k,v)

def __init__(self, engine_type, car_category, **kwags):
        super(car, self).__init__(engine_type, **kwags)     	
        self.car_category = car_category
        self.doors = 5
        self.wheel = 4


my_car = car ('VIN-120','saloon', 'engine_type' = 5       


