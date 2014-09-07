Android-Friendly NumPy and Matplotlib
=====================================

version 0.0.1 (07-Sep-2014)


ABOUT
-----

The NumPy and Matplotlib packages are absolutely awesome, and two
of my bestest friends. BUT! When compiling code to an Android .pkg
using the [PyGame subset for Android](http://pygame.renpy.org/index.html), they don't quite play nice.

Therefore, this project aims to provide an alternative to NumPy and
Matplotlib that is both slower and worse than the originals, but that
will work on Android. The idea is to re-write the NumPy functions in
pure Python, and to employ PyGame's graphical amazingness to replace
Matplotlib's drawing functions.


AIMS
----

The (initial) aim is simple: to provide an alternative to all
functions used in [CancellationTools](https://github.com/esdalmaijer/CancellationTools). But feel free to help out if
you see a potential implementation of these modules for other projects
as well.


USAGE
-----

~~~ .python
try:
	import android
except ImportError:
	android = None

if android == None:
	import numpy
else:
	import androidfriendly.numpy as numpy
~~~


ALTERNATIVE USAGE
-----------------

Not all function inputs can be correctly captured in pure Python, e.g.
NumPy's *where* function:

~~~ .python
>>> import numpy
>>> test = numpy.arange(5)
>>> test == 3
array([False, False, False,  True, False], dtype=bool)
>>> numpy.where(test == 3)
(array([3]),)
~~~

The equivalent using lists, would result in the following:

~~~ .python
>>> test = range(5)
>>> test == 3
False
~~~

Therefore, the *where* function's input is slightly different in the
Android-friendly libraries:

~~~ .python
>>> import androidfriendly.numpy as numpy
>>> test = numpy.arange(5)
>>> test == 3
False
>>> numpy.where(test, '==', 3)
[[3]]
~~~

This means there will have to be some re-writing of code to make Android
apps work with the Android-friendly NumPy:

~~~ .python
try:
	import android
except ImportError:
	android = None

if android == None:
	import numpy
else:
	import androidfriendly.numpy as numpy

test = numpy.arange(5)

if android == None:
	print(numpy.where(test == 3))
else:
	print(numpy.where(test, '==', 3))
~~~

If anybody knows a brilliant solution to this, please do let me know!
Another problem, that comes down to the same issue, is array arithmetic,
which works perfectly fine in NumPy:

~~~ .python
>>> a = numpy.arange(1,5,1)
>>> b = numpy.arange(5,1,-1)
>>> a - b
array([-4, -2,  0,  2])
~~~

But, of course, not so much in Android-friendly NumPy (where 'arrays'
are in fact lists):

~~~ .python
>>> a = numpy.arange(1,5,1)
>>> b = numpy.arange(5,1,-1)
>>> a - b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for -: 'list' and 'list'
~~~~

Again, brilliant solutions to this problem are very welcome!

