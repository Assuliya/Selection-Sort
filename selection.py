def selection(y,z): #Works if you add an empty list (goes where 'z' is)
	length = len(y)
	while len(z) != length:
		x = min(y)
		m = y.index(min(y))
		y[0],y[m]=y[m],y[0]
		z.append(y[0])
		print y
		print z
		y.pop(0)
		print y
		print z

base = []
copy = [] #an empty list that I use to push all of the sorted numbers

for i in range(100):
	import random
	base.append(random.randint(0,10000))
print base




print selection(base,copy)



