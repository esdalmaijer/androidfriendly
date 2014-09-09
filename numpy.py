import copy
import math
import pickle

# # # # #
# MISC

e = math.e
pi = math.pi
inf = float('inf')
nan = NaN = NAN = float('NaN')

normalmax = copy.deepcopy(max)
normalmin = copy.deepcopy(min)
normalsum = copy.deepcopy(sum)


# # # # #
# ARRAY CLASS

class Array(list):

	# GET/SET

	def __getitem__(self, y):
		
		if type(y) == int:
			return list.__getitem__(self, y)
		elif type(y) == slice:
			i = y.indices(self.__len__())
			return Array(self.__getslice__(i[0], i[1]))
		elif type(y) in [Array, list, tuple]:
			if len(y) == 2 and type(y[0]) == int and type(y[1]) == int:
				return list.__getitem__(self[y[0]], y[1])
			elif type(y[0]) == slice:
				outl = []
				xi = y[0].indices(self.__len__())
				for i in range(xi[0], xi[1]):
					yi = y[1].indices(self[i].__len__())
					outl.append(self[i].__getslice__(yi[0],yi[1]))
			elif self.__len__() == len(y):
				outl = []
				for i in range(self.__len__()):
					if y[i]:
						outl.append(list.__getitem__(self, i))
			else:
				raise Exception("ERROR in androidfriendly.numpy.Array.__getitem__: \
					vectors must be same length!")
			return Array(outl)
		else:
			raise Exception("ERROR in androidfriendly.numpy.Array.__getitem__: \
				provide integer index or Boolean Array/list/tuple of same length!")
	
	def __setitem__(self, i, y):
		
		if type(i) == int:
			list.__setitem__(self, i, y)
		elif type(i) in [Array, list, tuple]:
			list.__setitem__(self[i[0]], i[1], y)
	
	# RICH COMPARISONS
	
	def __lt__(self, y):
		
		outl = []
		if type(y) in [Array, tuple, list]:
			if self.__len__() == len(y):
				for i in range(self.__len__()):
					outl.append(self.__getitem__(i) < y[i])
			else:
				raise Exception("ERROR in androidfriendly.numpy.Array.__lt__: \
					vectors must be same length!")
		else:
			for i in range(self.__len__()):
				outl.append(self.__getitem__(i) < y)
		return Array(outl)
	
	def __le__(self, y):
		
		outl = []
		if type(y) in [Array, tuple, list]:
			if self.__len__() == len(y):
				for i in range(self.__len__()):
					outl.append(self.__getitem__(i) <= y[i])
			else:
				raise Exception("ERROR in androidfriendly.numpy.Array.__le__: \
					vectors must be same length!")
		else:
			for i in range(self.__len__()):
				outl.append(self.__getitem__(i) <= y)
		return Array(outl)
	
	def __eq__(self, y):
		
		outl = []
		if type(y) in [Array, tuple, list]:
			if self.__len__() == len(y):
				for i in range(self.__len__()):
					outl.append(self.__getitem__(i) == y[i])
			else:
				raise Exception("ERROR in androidfriendly.numpy.Array.__eq__: \
					vectors must be same length!")
		else:
			for i in range(self.__len__()):
				outl.append(self.__getitem__(i) == y)
		return Array(outl)
	
	def __ne__(self, y):
		
		outl = []
		if type(y) in [Array, tuple, list]:
			if self.__len__() == len(y):
				for i in range(self.__len__()):
					outl.append(self.__getitem__(i) <> y[i])
			else:
				raise Exception("ERROR in androidfriendly.numpy.Array.__ne__: \
					vectors must be same length!")
		else:
			for i in range(self.__len__()):
				outl.append(self.__getitem__(i) <> y)
		return Array(outl)
	
	def __gt__(self, y):
		
		outl = []
		if type(y) in [Array, tuple, list]:
			if self.__len__() == len(y):
				for i in range(self.__len__()):
					outl.append(self.__getitem__(i) > y[i])
			else:
				raise Exception("ERROR in androidfriendly.numpy.Array.__gt__: \
					vectors must be same length!")
		else:
			for i in range(self.__len__()):
				outl.append(self.__getitem__(i) > y)
		return Array(outl)
	
	def __ge__(self, y):
		
		outl = []
		if type(y) in [Array, tuple, list]:
			if self.__len__() == len(y):
				for i in range(self.__len__()):
					outl.append(self.__getitem__(i) >= y[i])
			else:
				raise Exception("ERROR in androidfriendly.numpy.Array.__ge__: \
					vectors must be same length!")
		else:
			for i in range(self.__len__()):
				outl.append(self.__getitem__(i) >= y)
		return Array(outl)
	
	# ARITHMETIC OPERATORS
	
	def __add__(self, y):
		
		# list to contain results of operation
		outl = []
		# Array and Array operation
		if type(y) in [Array, tuple, list]:
			if self.__len__() == len(y):
				for i in range(self.__len__()):
					outl.append(self.__getitem__(i) + y[i])
			else:
				raise Exception("ERROR in androidfriendly.numpy.Array.__add__: \
					vectors must be same length!")
		# Array and single value operation
		else:
			# go through own elements
			for i in range(self.__len__()):
				# if element self[i] is a number, a regular operation
				# will be performed; if self[i] is an Array, tuple, or
				# list, it will be passed to this function (support for
				# multiple dimensions by means of recursion)
				if type(self[i]) in [Array, tuple, list]:
					self[i] = Array(self[i])
				outl.append(self[i] + y)
		# after operations (potentially including recursions) have
		# concluded, return result
		return Array(outl)
	
	def __radd__(self, y):
		
		outl = []
		if type(y) in [Array, tuple, list]:
			if self.__len__() == len(y):
				for i in range(self.__len__()):
					outl.append(y[i] + self.__getitem__(i))
			else:
				raise Exception("ERROR in androidfriendly.numpy.Array.__radd__: \
					vectors must be same length!")
		else:
			for i in range(self.__len__()):
				if type(self[i]) in [Array, tuple, list]:
					self[i] = Array(self[i])
				outl.append(y + self[i])
		# after operations (potentially including recursions) have
		# concluded, return result
		return Array(outl)

	def __div__(self, y):
		
		outl = []
		if type(y) in [Array, tuple, list]:
			if self.__len__() == len(y):
				for i in range(self.__len__()):
					outl.append(self.__getitem__(i) / y[i])
			else:
				raise Exception("ERROR in androidfriendly.numpy.Array.__div__: \
					vectors must be same length!")
		else:
			for i in range(self.__len__()):
				if type(self[i]) in [Array, tuple, list]:
					self[i] = Array(self[i])
				outl.append(self[i] / y)
		return Array(outl)

	def __rdiv__(self, y):
		
		outl = []
		if type(y) in [Array, tuple, list]:
			if self.__len__() == len(y):
				for i in range(self.__len__()):
					outl.append(y[i] / self.__getitem__(i))
			else:
				raise Exception("ERROR in androidfriendly.numpy.Array.__rdiv__: \
					vectors must be same length!")
		else:
			for i in range(self.__len__()):
				if type(self[i]) in [Array, tuple, list]:
					self[i] = Array(self[i])
				outl.append(y / self[i])
		return Array(outl)
	
	def __floordiv__(self, y):
		
		outl = []
		if type(y) in [Array, tuple, list]:
			if self.__len__() == len(y):
				for i in range(self.__len__()):
					outl.append(self.__getitem__(i).__floordiv__(y[i]))
			else:
				raise Exception("ERROR in androidfriendly.numpy.Array.__floordiv__: \
					vectors must be same length!")
		else:
			for i in range(self.__len__()):
				if type(self[i]) in [Array, tuple, list]:
					self[i] = Array(self[i])
				outl.append(self[i].__floordiv__(y))
		return Array(outl)
	
	def __rfloordiv__(self, y):
		
		outl = []
		if type(y) in [Array, tuple, list]:
			if self.__len__() == len(y):
				for i in range(self.__len__()):
					outl.append(self.__getitem__(i).__rfloordiv__(y[i]))
			else:
				raise Exception("ERROR in androidfriendly.numpy.Array.__rfloordiv__: \
					vectors must be same length!")
		else:
			for i in range(self.__len__()):
				if type(self[i]) in [Array, tuple, list]:
					self[i] = Array(self[i])
				outl.append(self[i].__rfloordiv__(y))
		return Array(outl)
	
	def __mod__(self, y):
		
		outl = []
		if type(y) in [Array, tuple, list]:
			if self.__len__() == len(y):
				for i in range(self.__len__()):
					outl.append(self.__getitem__(i) % y[i])
			else:
				raise Exception("ERROR in androidfriendly.numpy.Array.__mod__: \
					vectors must be same length!")
		else:
			for i in range(self.__len__()):
				if type(self[i]) in [Array, tuple, list]:
					self[i] = Array(self[i])
				outl.append(self[i] % y)
		return Array(outl)
	
	def __rmod__(self, y):
		
		outl = []
		if type(y) in [Array, tuple, list]:
			if self.__len__() == len(y):
				for i in range(self.__len__()):
					outl.append(y[i] % self.__getitem__(i))
			else:
				raise Exception("ERROR in androidfriendly.numpy.Array.__rmod__: \
					vectors must be same length!")
		else:
			for i in range(self.__len__()):
				if type(self[i]) in [Array, tuple, list]:
					self[i] = Array(self[i])
				outl.append(y % self[i])
		return Array(outl)
	
	def __mul__(self, y):
		
		outl = []
		if type(y) in [Array, tuple, list]:
			if self.__len__() == len(y):
				for i in range(self.__len__()):
					outl.append(self.__getitem__(i) * y[i])
			else:
				raise Exception("ERROR in androidfriendly.numpy.Array.__mul__: \
					vectors must be same length!")
		else:
			for i in range(self.__len__()):
				if type(self[i]) in [Array, tuple, list]:
					self[i] = Array(self[i])
				outl.append(self[i] * y)
		return Array(outl)
	
	def __rmul__(self, y):
		
		outl = []
		if type(y) in [Array, tuple, list]:
			if self.__len__() == len(y):
				for i in range(self.__len__()):
					outl.append(y[i] * self.__getitem__(i))
			else:
				raise Exception("ERROR in androidfriendly.numpy.Array.__rmul__: \
					vectors must be same length!")
		else:
			for i in range(self.__len__()):
				if type(self[i]) in [Array, tuple, list]:
					self[i] = Array(self[i])
				outl.append(y * self[i])
		return Array(outl)
	
	def __neg__(self):
		
		outl = []
		for i in range(self.__len__()):
			if type(self[i]) in [Array, tuple, list]:
				self[i] = Array(self[i])
			print self[i]
			if self[i] > 0:
				outl.append(self[i] * -1)
			else:
				outl.append(self[i])
		return Array(outl)

	def __pos__(self):
		
		outl = []
		for i in range(self.__len__()):
			if type(self[i]) in [Array, tuple, list]:
				self[i] = Array(self[i])
			if self[i] < 0:
				outl.append(self[i] * -1)
			else:
				outl.append(self[i])
		return Array(outl)
	
	def __pow__(self, y):
		
		outl = []
		if type(y) in [Array, tuple, list]:
			if self.__len__() == len(y):
				for i in range(self.__len__()):
					outl.append(self.__getitem__(i) ** y[i])
			else:
				raise Exception("ERROR in androidfriendly.numpy.Array.__pow__: \
					vectors must be same length!")
		else:
			for i in range(self.__len__()):
				if type(self[i]) in [Array, tuple, list]:
					self[i] = Array(self[i])
				outl.append(self[i] ** y)
		return Array(outl)
	
	def __rpow__(self, y):
		
		outl = []
		if type(y) in [Array, tuple, list]:
			if self.__len__() == len(y):
				for i in range(self.__len__()):
					outl.append(y[i] ** self.__getitem__(i))
			else:
				raise Exception("ERROR in androidfriendly.numpy.Array.__rpow__: \
					vectors must be same length!")
		else:
			for i in range(self.__len__()):
				if type(self[i]) in [Array, tuple, list]:
					self[i] = Array(self[i])
				outl.append(y ** self[i])
		return Array(outl)
	
	def __sub__(self, y):
		
		outl = []
		if type(y) in [Array, tuple, list]:
			if self.__len__() == len(y):
				for i in range(self.__len__()):
					outl.append(self.__getitem__(i) - y[i])
			else:
				raise Exception("ERROR in androidfriendly.numpy.Array.__sub__: \
					vectors must be same length!")
		else:
			for i in range(self.__len__()):
				if type(self[i]) in [Array, tuple, list]:
					self[i] = Array(self[i])
				outl.append(self[i] - y)
		return Array(outl)
	
	def __rsub__(self, y):
		
		outl = []
		if type(y) in [Array, tuple, list]:
			if self.__len__() == len(y):
				for i in range(self.__len__()):
					outl.append(y[i] - self.__getitem__(i))
			else:
				raise Exception("ERROR in androidfriendly.numpy.Array.__rsub__: \
					vectors must be same length!")
		else:
			for i in range(self.__len__()):
				if type(self[i]) in [Array, tuple, list]:
					self[i] = Array(self[i])
				outl.append(y - self[i])
		return Array(outl)
	
	def __truediv__(self, y):
		
		outl = []
		if type(y) in [Array, tuple, list]:
			if self.__len__() == len(y):
				for i in range(self.__len__()):
					outl.append(self.__getitem__(i) / float(y[i]))
			else:
				raise Exception("ERROR in androidfriendly.numpy.Array.__mul__: \
					vectors must be same length!")
		else:
			for i in range(self.__len__()):
				if type(self[i]) in [Array, tuple, list]:
					self[i] = Array(self[i])
				outl.append(self[i] / float(y))
		return Array(outl)
	
	def __rtruediv__(self, y):
		
		outl = []
		if type(y) in [Array, tuple, list]:
			if self.__len__() == len(y):
				for i in range(self.__len__()):
					outl.append(float(y[i]) / self.__getitem__(i))
			else:
				raise Exception("ERROR in androidfriendly.numpy.Array.__rmul__: \
					vectors must be same length!")
		else:
			for i in range(self.__len__()):
				if type(self[i]) in [Array, tuple, list]:
					self[i] = Array(self[i])
				outl.append(float(y) / self[i])
		return Array(outl)


# # # # #
# RE-DEFINITIONS

def abs(l):
	
	if type(l) in [int, float]:
		return (l**2)**0.5
	
	else:
		outl = []
		for i in range(len(l)):
			if type(l[i]) in [Array, list, tuple]:
				l[i] = Array(l[i])
			outl.append(abs(l[i]))
		return Array(outl)

def arange(start, stop=None, step=1):
	
	if stop == None:
		stop = copy.copy(start)
		start = 0
	
	return range(start, stop, step)


def argmin(l):
	
	li = 0	
	for i in range(len(l)):
		if l[i] < l[li]:
			li = copy.copy(i)

	return li


def array(l, dtype=None):
	
	if dtype == None:
		return Array(l)
	
	else:
		if type(l) not in [Array, list, tuple]:
			for strdt in ['int', 'str', 'float']:
				exec("dt = %s" % strdt)
				if dt == dtype or strdt in str(dtype):
					return dt(l)
			raise Exception("ERROR in androidfriendly.numpy.array: \
				unknown dtype '%s'" % dtype)
		outl = []
		for i in range(len(l)):
			if type(l[i]) in [Array, list, tuple]:
				l[i] = Array(l[i])
			outl.append(array(l[i], dtype=dtype))
		return Array(outl)


def asarray(l, dtype=None):
	
	return array(l, dtype=dtype)
	

def diff(l):
	
	outl = []
	for i in range(len(l)-1):
		outl.append(l[i+1] - l[i])
	
	return Array(outl)


def exp(l):
	
	if type(l) in [int, float]:

		return math.e ** l

	elif type(l) in [Array, tuple, list]:

		return math.e ** Array(l)

	else:
		raise Exception("ERROR in androidfriendly.numpy.exp: unrecognized \
			data type; please pass integer, float, or Array")


def ceil(l):
	
	if type(l) not in [Array, list, tuple]:
		if l - int(l) == 0:
			return int(l)
		else:
			return int(l) + 1
	else:
		outl = []
		for i in range(len(l)):
			if type(l[i]) in [Array, list, tuple]:
				l[i] = Array(l[i])
			outl.append(ceil(l[i]))
		return Array(outl)


def floor(l):
	
	if type(l) not in [Array, list, tuple]:
		return int(l)
	else:
		outl = []
		for i in range(len(l)):
			if type(l[i]) in [Array, list, tuple]:
				l[i] = Array(l[i])
			outl.append(floor(l[i]))
		return Array(outl)


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

	return Array(same)


def load(filename):
	
	filename = filename.replace('.npy', '.afnpy')
	f = open(filename, 'r')
	l = pickle.load(f)
	f.close()
	
	return l


def max(l):
	
	if type(l[0]) in [float, int]:
		return normalmax(l)
	else:
		for i in range(len(l)):
			omax = 0
			if type(l[i]) in [Array, list, tuple]:
				l[i] = Array(l[i])
			lmax = max(l[i])
			if lmax > omax:
				omax = copy.copy(lmax)
		return omax


def mean(l):
	
	return sum(l) / float(size(l))


def min(l):
	
	if type(l[0]) in [float, int]:
		return normalmin(l)
	else:
		for i in range(len(l)):
			omin = inf
			if type(l[i]) in [Array, list, tuple]:
				l[i] = Array(l[i])
			lmin = min(l[i])
			if lmin < omin:
				omin = copy.copy(lmin)
		return omin


def nanmean(l):

	return float(nansum(l)) / nansize(l)


def nansize(l):
	
	if type(l[0]) in [int, float]:
		nonan = []
		for n in l:
			if not math.isnan(n):
				nonan.append(n)
		return len(nonan)
	else:
		s = 0
		for i in range(len(l)):
			if l[i] in [Array, list, float]:
				l[i] = Array(l[i])
			s += nansize(l[i])
		return s


def nansum(l):
	
	if type(l[0]) in [int, float]:
		nonan = []
		for n in l:
			if not math.isnan(n):
				nonan.append(n)
		return normalsum(nonan)
	else:
		s = 0
		for i in range(len(l)):
			if l[i] in [Array, list, float]:
				l[i] = Array(l[i])
			s += nansum(l[i])
		return s


def resize(l, newdims):
	
	# TODO: support for arrays of more than 2 dimensions
	if len(l) != newdims[0] * newdims[1]:
		raise Exception("ERROR in androidfriendly.numpy.resize: \
			lenght of array (%d) does not match resized matrix size (%d)" % (len(l)), newdims[0] * newdims[1])
	i = 0
	outl = []
	for x in range(newdims[0]):
		outl.append([])
		for y in range(newdims[1]):
			outl[x].append(l[i])
			i += 1
	return Array(outl)


def save(filename, l):
	
	filename = filename.replace('.npy', '.afnpy')
	f = open(filename, 'w')
	pickle.dump(l, f)
	f.close()


def sqrt(l):
	
	return l ** 0.5


def shape(l):
	
	s = []
	lst = l[:]
	while True:
		if type(lst) in [Array, list, tuple]:
			s.append(len(lst))
			lst = lst[0]
		else:
			break
	return Array(s)


def size(l, axis=None):
	
	s = shape(l)
	if axis == None:
		c = s[0]
		for i in range(1, len(s)):
			c *= s[i]
	# TODO: count number of recursions, until i == axis, then return len
	elif axis == 0:
		c = len(l)
	elif axis == 1:
		c = len(l[0])
	elif axis == 2:
		c = len(l[0][0])
	else:
		raise Exception("ERROR in androidfriendly.numpy.size: no support for \
			matrices with over three dimensions when using the axis keyword")
	return c


def sum(l):
	
	if type(l[0]) in [int, float]:
		return normalsum(l)
	else:
		s = 0
		for i in range(len(l)):
			if l[i] in [Array, list, float]:
				l[i] = Array(l[i])
			s += sum(l[i])
		return s


def unique(l):
	
	outl = []
	for e in l:
		if e not in outl:
			outl.append(e)
	outl.sort()
	return Array(outl)
	

def where(conditional):
	
	outl = []
	for i in range(len(conditional)):
		if conditional[i]:
			outl.append(i)
	return Array([Array(outl)])


def zeros(N, dtype=None):
	
	if type(N) == int:
		return array([0] * N, dtype=dtype)

	else:
		outl = []
		for i in range(N[0]):
			newN = N[1:]
			if len(N[1:]) == 1:
				newN = N[1]
			outl.append(zeros(newN))
		return array(outl, dtype=dtype)
