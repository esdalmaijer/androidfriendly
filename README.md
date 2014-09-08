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

Currently, this means that arrays are usually assumed to be a vector;
matrices (vectors of vectors of vectors etc.) are not supported in
all functions yet.


USAGE
-----

~~~ .python
# try importing android
try:
	import android
except ImportError:
	android = None

# if android could not be imported, we are not on
# android, so we do not have to bother with importing
# android-friendly numpy
if android == None:
	import numpy
else:
	import androidfriendly.numpy as numpy
~~~

You can create arrays as you would do using NumPy:

~~~ .python
>>> a = numpy.array([1,2,3])
>>> b = numpy.array([3,2,1])
~~~

Calculations are the same:

~~~ .python
>>> a + b
[4, 4, 4]

>>> a - b
[-2, 0, 2]

>>> a * b
[3, 4, 3]

>>> a / b
[0.3333333333333333, 1.0, 3.0]

>>> a ** b
[1, 4, 3]
~~~

And so are comparisons:

~~~ .python
>>> a < b
[True, False, False]
>>> a <= b
[True, True, False]
>>> a == b
[False, True, False]
>>> a != b
[True, False, True]
>>> a > b
[False, False, True]
>>> a >= b
[False, True, True]
~~~

