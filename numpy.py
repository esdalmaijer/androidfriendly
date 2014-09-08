import copy
import math

# # # # #
# MISC

e = math.e
pi = math.pi
nan = NaN = NAN = 'NaN'


# # # # #
# NATIVE FUNCTIONS

# define the max function as the regular max function, so that numpy.max()
# behaves the same as max() (same for min)
max = max
min = min


# # # # #
# ARRAY CLASS

class Array(list):
	
	# RICH COMPARISONS
	
	def __lt__(self, y):
		
		outl = []
		if self.__len__() == len(y):
			for i in range(self.__len__()):
				outl.append(self.__getitem__(i) < y[i])
		else:
			raise Exception("ERROR in androidfriendly.numpy.Array.__lt__: \
				vectors must be same length!")
		return outl
	
	def __le__(self, y):
		
		outl = []
		if self.__len__() == len(y):
			for i in range(self.__len__()):
				outl.append(self.__getitem__(i) <= y[i])
		else:
			raise Exception("ERROR in androidfriendly.numpy.Array.__le__: \
				vectors must be same length!")
		return outl
	
	def __eq__(self, y):
		
		outl = []
		if self.__len__() == len(y):
			for i in range(self.__len__()):
				outl.append(self.__getitem__(i) == y[i])
		else:
			raise Exception("ERROR in androidfriendly.numpy.Array.__eq__: \
				vectors must be same length!")
		return outl
	
	def __ne__(self, y):
		
		outl = []
		if self.__len__() == len(y):
			for i in range(self.__len__()):
				outl.append(self.__getitem__(i) <> y[i])
		else:
			raise Exception("ERROR in androidfriendly.numpy.Array.__ne__: \
				vectors must be same length!")
		return outl
	
	def __gt__(self, y):
		
		outl = []
		if self.__len__() == len(y):
			for i in range(self.__len__()):
				outl.append(self.__getitem__(i) > y[i])
		else:
			raise Exception("ERROR in androidfriendly.numpy.Array.__gt__: \
				vectors must be same length!")
		return outl
	
	def __ge__(self, y):
		
		outl = []
		if self.__len__() == len(y):
			for i in range(self.__len__()):
				outl.append(self.__getitem__(i) >= y[i])
		else:
			raise Exception("ERROR in androidfriendly.numpy.Array.__ge__: \
				vectors must be same length!")
		return outl
	
	# ARITHMETIC OPERATORS
	
	def __add__(self, y):
		
		outl = []
		if self.__len__() == len(y):
			for i in range(self.__len__()):
				outl.append(self.__getitem__(i) + y[i])
		else:
			raise Exception("ERROR in androidfriendly.numpy.Array.__add__: \
				vectors must be same length!")
		return outl

	def __div__(self, y):
		
		outl = []
		if self.__len__() == len(y):
			for i in range(self.__len__()):
				outl.append(self.__getitem__(i) / y[i])
		else:
			raise Exception("ERROR in androidfriendly.numpy.Array.__div__: \
				vectors must be same length!")
		return outl
	
	def __floordiv__(self, y):
		
		outl = []
		if self.__len__() == len(y):
			for i in range(self.__len__()):
				outl.append(self.__getitem__(i).__floordiv__(y[i]))
		else:
			raise Exception("ERROR in androidfriendly.numpy.Array.__floordiv__: \
				vectors must be same length!")
		return outl
	
	def __mod__(self, y):
		
		outl = []
		if self.__len__() == len(y):
			for i in range(self.__len__()):
				outl.append(self.__getitem__(i) % y[i])
		else:
			raise Exception("ERROR in androidfriendly.numpy.Array.__mod__: \
				vectors must be same length!")
		return outl
	
	def __mul__(self, y):
		
		outl = []
		if self.__len__() == len(y):
			for i in range(self.__len__()):
				outl.append(self.__getitem__(i) * y[i])
		else:
			raise Exception("ERROR in androidfriendly.numpy.Array.__mul__: \
				vectors must be same length!")
		return outl
	
	def __neg__(self):
		
		outl = []
		for i in range(self.__len__()):
			if self.__getitem__(i) > 0:
				outl.append(self.__getitem__(i) * -1)
			else:
				outl.append(self.__getitem__(i))
		return outl

	def __pos__(self):
		
		outl = []
		for i in range(self.__len__()):
			if self.__getitem__(i) < 0:
				outl.append(self.__getitem__(i) * -1)
			else:
				outl.append(self.__getitem__(i))
		return outl
	
	def __pow__(self, y):
		
		outl = []
		if self.__len__() == len(y):
			for i in range(self.__len__()):
				outl.append(self.__getitem__(i) ** y[i])
		else:
			raise Exception("ERROR in androidfriendly.numpy.Array.__pow__: \
				vectors must be same length!")
		return outl
	
	def __sub__(self, y):
		
		outl = []
		if self.__len__() == len(y):
			for i in range(self.__len__()):
				outl.append(self.__getitem__(i) - y[i])
		else:
			raise Exception("ERROR in androidfriendly.numpy.Array.__sub__: \
				vectors must be same length!")
		return outl
	
	def __truediv__(self, y):
		
		outl = []
		if self.__len__() == len(y):
			for i in range(self.__len__()):
				outl.append(self.__getitem__(i) / float(y[i]))
		else:
			raise Exception("ERROR in androidfriendly.numpy.Array.__mul__: \
				vectors must be same length!")
		return outl


# # # # #
# RE-DEFINITIONS

def arange(start, stop=None, step=1):
	
	if stop == None:
		stop = copy.copy(start)
		start = 0
	
	return range(start, stop, step)


def argmin(l):
	
	li = 0	
	for i in range(len(l)):
		if l[i] < l[li]:
			li = copy(i)

	return li


def array(l):
	
	return Array(l)


def asaray(l):
	
	return Array(l)
	

def diff(l):
	
	outl = []
	for i in range(len(l)-1):
		outl.append(l[i+1] - l[i])
	
	return outl


def exp(l):
	
	if type(l) in [int, float]:

		return math.e ** l

	elif type(l) in [tuple, list]:
		ndim = len(shape(l))
		if ndim < 4:
			outl = []
			if ndim > 1:
				outl.append([]*len(l))
				for i in range(len(outl)):
					outl[i].append([]*len(l[0]))
					if ndim > 2:
						for j in range(len(l[0])):
							outl[i][j].append([]*len(l[0][0]))
							for k in range(len(l[0][0])):
								outl[i][j].append(math.e ** l[i][j][k])
					else:
						for j in range(len(l[0])):
							outl[i].append(math.e ** l[i][j])
			else:
				for i in range(len(l)):
					outl.append(math.e ** l[i])
		else:
			raise Exception("ERROR in androidfriendly.numpy.exp: array operation \
				for more tha 3 dimensions not implemented yet, please pass \
				one value at a time for larger structures")
	else:
		raise Exception("ERROR in androidfriendly.numpy.exp: unrecognized \
			data type; please pass integer, float, or list")
	
	return outl


def ceil(number):
	
	return int(number)


def floor(number):
	
	return int(number) - 1


def intersect1d(l1, l2):
	
	"""Returns the sorted, unique values that are in both arrays
	"""
	
	# go through all values of list 1
	same = []
	for i in range(len(l1)):
		# store the current value if it is in list 2, but not in same yet
		if l1[i] in l2[i] and l1[i] not in same:
			same.append(l1[i])
	# sort same
	same.sort()

	return same


def load(filename):
	# TODO: unpickle list
	pass


def mean(l):
	
	s = 0
	n = 0
	for number in l:
		n += 1
		s += number
	
	return float(s) / n


def nanmax(l):

	s = 0
	n = 0
	for number in l:
		if number != NaN:
			n += 1
			s += number
	
	return float(s) / n


def nansum(l):

	s = 0
	for number in l:
		if number != NaN:
			s += number
	
	return s


def resize(l, newdims):
	# TODO: This, but how?
	pass


def save(filename, l):
	# TODO: pickle list
	pass


def sqrt(l):
	
	if type(l) in [int, float]:

		return l ** 0.5

	elif type(l) in [tuple, list]:
		ndim = len(shape(l))
		if ndim < 4:
			outl = []
			if ndim > 1:
				outl.append([]*len(l))
				for i in range(len(outl)):
					outl[i].append([]*len(l[0]))
					if ndim > 2:
						for j in range(len(l[0])):
							outl[i][j].append([]*len(l[0][0]))
							for k in range(len(l[0][0])):
								outl[i][j].append(l[i][j][k] ** 0.5)
					else:
						for j in range(len(l[0])):
							outl[i].append(l[i][j] ** 0.5)
			else:
				for i in range(len(l)):
					outl.append(l[i] ** 0.5)
		else:
			raise Exception("ERROR in androidfriendly.numpy.sqrt: array operation \
				for more tha 3 dimensions not implemented yet, please pass \
				one value at a time for larger structures")
	else:
		raise Exception("ERROR in androidfriendly.numpy.sqrt: unrecognized \
			data type; please pass integer, float, or list")
	
	return outl


def shape(l):
	
	s = []
	lst = l[:]
	while True:
		if type(lst) in [list, tuple]:
			s.append(len(lst))
			lst = lst[0]
		else:
			break
	return s


def size(l):
	
	s = shape(l)
	c = s[0]
	for i in range(1, len(s)):
		c *= s[i]
	
	return c
	

def where(conditional):
	
	outl = []
	for i in range(len(conditional)):
		if conditional[i]:
			outl.append(i)
	return [outl]


def zeros(N):
	
	return [0] * N
	