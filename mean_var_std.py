import numpy as np

def mn(mat, calculations):
	for j in range(3):
		if j == 0:
			x = np.mean(mat, axis = 0)
			y = x.tolist()
			calculations['mean'].append(y)

		elif j == 1:
			x = np.mean(mat, axis = 1)
			y = x.tolist()
			calculations['mean'].append(y)

		elif j == 2:
			x = np.mean(mat, axis = None)
			y = x.tolist()
			calculations['mean'].append(y) 

	return (mat, calculations)

def var(mat, calculations):
	for j in range(3):
		if j == 0:
			x = np.var(mat, axis = 0)
			y = x.tolist()
			calculations['variance'].append(y)

		elif j == 1:
			x = np.var(mat, axis = 1)
			y = x.tolist()
			calculations['variance'].append(y)

		elif j == 2:
			x = np.var(mat, axis = None)
			y = x.tolist()
			calculations['variance'].append(y)

	return (mat, calculations)

def stdev(mat, calculations):
	for j in range(3):
		if j == 0:
			x = np.std(mat, axis = 0)
			y = x.tolist()
			calculations['standard deviation'].append(y)

		elif j == 1:
			x = np.std(mat, axis = 1)
			y = x.tolist()
			calculations['standard deviation'].append(y)

		elif j == 2:
			x = np.std(mat, axis = None)
			y = x.tolist()
			calculations['standard deviation'].append(y) 
	
	return (mat, calculations)

def maxim(mat, calculations):
	for j in range(3):
		if j == 0:
			x = np.max(mat, axis = 0)
			y = x.tolist()
			calculations['max'].append(y)

		elif j == 1:
			x = np.max(mat, axis = 1)
			y = x.tolist()
			calculations['max'].append(y)

		elif j == 2:
			x = np.max(mat, axis = None)
			y = x.tolist()
			calculations['max'].append(y) 
	
	return (mat, calculations)

def minim(mat, calculations):
	for j in range(3):
		if j == 0:
			x = np.min(mat, axis = 0)
			y = x.tolist()
			calculations['min'].append(y)

		elif j == 1:
			x = np.min(mat, axis = 1)
			y = x.tolist()
			calculations['min'].append(y)

		elif j == 2:
			x = np.min(mat, axis = None)
			y = x.tolist()
			calculations['min'].append(y) 

	return (mat, calculations)

def total(mat, calculations):
	for j in range(3):
		if j == 0:
			x = np.sum(mat, axis = 0)
			y = x.tolist()
			calculations['sum'].append(y)

		elif j == 1:
			x = np.sum(mat, axis = 1)
			y = x.tolist()
			calculations['sum'].append(y)

		elif j == 2:
			x = np.sum(mat, axis = None)
			y = x.tolist()
			calculations['sum'].append(y) 

	return (mat, calculations)

def calculate(ls):
	if len(ls) != 9:
		raise ValueError("List must contain nine numbers.")
	b = np.array(ls)
	mat = np.reshape(b, (3,3))

	calculations = {'mean': [],
			'variance': [],
			'standard deviation': [],
			'max': [],
			'min': [],
			'sum': []}
	
	for i in range(len(calculations)):
		if i == 0:
			mn(mat, calculations)
		elif i == 1:
			var(mat, calculations)
		elif i == 2:
			stdev(mat, calculations)
		elif i == 3:
			maxim(mat, calculations)
		elif i == 4:
			minim(mat, calculations)
		elif i == 5:
			total(mat, calculations)

	return calculations