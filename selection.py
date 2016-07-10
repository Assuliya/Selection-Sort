def selection(y,z): #Works if you add an empty list goes in (z)
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



base = [2,5,8,3,1]
copy = []


print selection(base,copy)



