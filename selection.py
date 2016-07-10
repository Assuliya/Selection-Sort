def selection(y,z): #Works if you add an empty list (goes where 'z' is)
	length = len(y) 
	print y
	while len(z) != length:
		
		w = y.index(min(y))
		y[0],y[w]=y[w],y[0]
		z.append(y[0])
		y.pop(0)

		print y
		print z

def selection2(y,z): #Version 2: Maximum
	length = len(y) 
	c = -1
	print y
	while len(z) != length:
		
		b = y.index(max(y))
		y[-1],y[b] = y[b],y[-1]
		z.insert(c,y[-1])
		c-=1
		y.pop(-1)

		print y
		print z

base = []
copy = [] #an empty list that I use to push all of the sorted numbers

for i in range(5):
	import random
	base.append(random.randint(0,10))
print base




print selection(base,copy) #print selection2(base,copy) #for Max



