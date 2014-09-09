# -*- coding: utf-8 -*-
#
# This file is part of CancellationTools
#
# CancellationTools is open-source software for running cancellation tasks,
# and directly analysing the data they produce.
#
# Copyright (C) 2014, Edwin S. Dalmaijer
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>

__author__ = u"Edwin Dalmaijer"

import struct
import pygame


def check_colour(colour):
	
	"""Checks if the passed colour is a correct one, and returns an RGB gun of
	that colour

	arguments
	
	colour		--	any kind of colour (RGB, hex, string) to check
	
	returns
	
	rgbcol		--	a RGB list of values between 0 and 255, e.g.
					[0,255,100]
	"""
	
	rgbcol = None
	err = None
	
	# check if the passed colour is a string
	if type(colour) in [str,unicode]:
		# check if the passed colour is a hex value
		if colour[0] == '#' and len(colour) == 7:
			# try converting hex to RGB
			try:
				# note: do NOT turn 'BBB' into unicode! (will cause error)
				rgbcol = list(struct.unpack('BBB', colour[1:].decode('hex')))
			except:
				err = u"colour '%s' not recognized"	
		else:
			# check if the colour is in the PyGame colour dict
			if colour in pygame.colordict.THECOLORS.keys():
				rgbcol = list(pygame.colordict.THECOLORS[colour][:3])
			else:
				err = u"colour '%s' not recognized" % colour
	# check if the passed colour is a string or a list
	elif type(colour) in [tuple,list]:
		rgbcol = list(colour[:3])
	# if the type of colour is something else, we don't know what to do
	else:
		err = u"colour '%s' not recognized"

	# check if the colour values are valid
	if err == None:
		if not sum(map(isrgb, rgbcol)) == 3:
			err = u"colour '%s' (RGB='%s') contains an illegal value" % (colour,rgbcol)

	# return an error if necessary
	if err != None:
		return err
	# return RGB gun is there are no errors
	else:
		return rgbcol


def isrgb(value):
	
	"""Checks if a value is between 0 and 255 (inlcuding 0 and 255)
	
	arguments
	
	value		--	a numerical value
	
	returns
	
	check		--	1 if the value is in range(0,256) or 0 if it is not
	"""
	
	if 0 <= int(value) <= 255:
		return 1
	else:
		return 0

		
# COLOURS
# these colours are all from the Tango theme, see:
# http://tango.freedesktop.org/Tango_Icon_Theme_Guidelines#Color_Palette
colours = {		u'butter': 	[		u'#fce94f',
							u'#edd400',
							u'#c4a000'],
			u'orange': 	[		u'#fcaf3e',
							u'#f57900',
							u'#ce5c00'],
			u'chocolate': 	[	u'#e9b96e',
							u'#c17d11',
							u'#8f5902'],
			u'chameleon': 	[	u'#8ae234',
							u'#73d216',
							u'#4e9a06'],
			u'skyblue': 	[	u'#729fcf',
							u'#3465a4',
							u'#204a87'],
			u'plum': 		[	u'#ad7fa8',
							u'#75507b',
							u'#5c3566'],
			u'scarletred':	[	u'#ef2929',
							u'#cc0000',
							u'#a40000'],
			u'aluminium':	[	u'#eeeeec',
							u'#d3d7cf',
							u'#babdb6',
							u'#888a85',
							u'#555753',
							u'#2e3436']
						}
# hex2rgb
for cn in colours.keys():
	for i in range(len(colours[cn])):
		colours[cn][i] = check_colour(colours[cn][i])


# COLOURMAP
colourmaps = {'jet':	[	(0,0,127),
					(0,0,132),
					(0,0,136),
					(0,0,141),
					(0,0,145),
					(0,0,150),
					(0,0,154),
					(0,0,159),
					(0,0,163),
					(0,0,168),
					(0,0,172),
					(0,0,177),
					(0,0,182),
					(0,0,186),
					(0,0,191),
					(0,0,195),
					(0,0,200),
					(0,0,204),
					(0,0,209),
					(0,0,213),
					(0,0,218),
					(0,0,222),
					(0,0,227),
					(0,0,232),
					(0,0,236),
					(0,0,241),
					(0,0,245),
					(0,0,250),
					(0,0,254),
					(0,0,255),
					(0,0,255),
					(0,0,255),
					(0,0,255),
					(0,4,255),
					(0,8,255),
					(0,12,255),
					(0,16,255),
					(0,20,255),
					(0,24,255),
					(0,28,255),
					(0,32,255),
					(0,36,255),
					(0,40,255),
					(0,44,255),
					(0,48,255),
					(0,52,255),
					(0,56,255),
					(0,60,255),
					(0,64,255),
					(0,68,255),
					(0,72,255),
					(0,76,255),
					(0,80,255),
					(0,84,255),
					(0,88,255),
					(0,92,255),
					(0,96,255),
					(0,100,255),
					(0,104,255),
					(0,108,255),
					(0,112,255),
					(0,116,255),
					(0,120,255),
					(0,124,255),
					(0,128,255),
					(0,132,255),
					(0,136,255),
					(0,140,255),
					(0,144,255),
					(0,148,255),
					(0,152,255),
					(0,156,255),
					(0,160,255),
					(0,164,255),
					(0,168,255),
					(0,172,255),
					(0,176,255),
					(0,180,255),
					(0,184,255),
					(0,188,255),
					(0,192,255),
					(0,196,255),
					(0,200,255),
					(0,204,255),
					(0,208,255),
					(0,212,255),
					(0,216,255),
					(0,220,254),
					(0,224,250),
					(0,228,247),
					(2,232,244),
					(5,236,241),
					(8,240,237),
					(12,244,234),
					(15,248,231),
					(18,252,228),
					(21,255,225),
					(24,255,221),
					(28,255,218),
					(31,255,215),
					(34,255,212),
					(37,255,208),
					(41,255,205),
					(44,255,202),
					(47,255,199),
					(50,255,195),
					(54,255,192),
					(57,255,189),
					(60,255,186),
					(63,255,183),
					(66,255,179),
					(70,255,176),
					(73,255,173),
					(76,255,170),
					(79,255,166),
					(83,255,163),
					(86,255,160),
					(89,255,157),
					(92,255,154),
					(95,255,150),
					(99,255,147),
					(102,255,144),
					(105,255,141),
					(108,255,137),
					(112,255,134),
					(115,255,131),
					(118,255,128),
					(121,255,125),
					(124,255,121),
					(128,255,118),
					(131,255,115),
					(134,255,112),
					(137,255,108),
					(141,255,105),
					(144,255,102),
					(147,255,99),
					(150,255,95),
					(154,255,92),
					(157,255,89),
					(160,255,86),
					(163,255,83),
					(166,255,79),
					(170,255,76),
					(173,255,73),
					(176,255,70),
					(179,255,66),
					(183,255,63),
					(186,255,60),
					(189,255,57),
					(192,255,54),
					(195,255,50),
					(199,255,47),
					(202,255,44),
					(205,255,41),
					(208,255,37),
					(212,255,34),
					(215,255,31),
					(218,255,28),
					(221,255,24),
					(224,255,21),
					(228,255,18),
					(231,255,15),
					(234,255,12),
					(237,255,8),
					(241,252,5),
					(244,248,2),
					(247,244,0),
					(250,240,0),
					(254,237,0),
					(255,233,0),
					(255,229,0),
					(255,226,0),
					(255,222,0),
					(255,218,0),
					(255,215,0),
					(255,211,0),
					(255,207,0),
					(255,203,0),
					(255,200,0),
					(255,196,0),
					(255,192,0),
					(255,189,0),
					(255,185,0),
					(255,181,0),
					(255,177,0),
					(255,174,0),
					(255,170,0),
					(255,166,0),
					(255,163,0),
					(255,159,0),
					(255,155,0),
					(255,152,0),
					(255,148,0),
					(255,144,0),
					(255,140,0),
					(255,137,0),
					(255,133,0),
					(255,129,0),
					(255,126,0),
					(255,122,0),
					(255,118,0),
					(255,115,0),
					(255,111,0),
					(255,107,0),
					(255,103,0),
					(255,100,0),
					(255,96,0),
					(255,92,0),
					(255,89,0),
					(255,85,0),
					(255,81,0),
					(255,77,0),
					(255,74,0),
					(255,70,0),
					(255,66,0),
					(255,63,0),
					(255,59,0),
					(255,55,0),
					(255,52,0),
					(255,48,0),
					(255,44,0),
					(255,40,0),
					(255,37,0),
					(255,33,0),
					(255,29,0),
					(255,26,0),
					(255,22,0),
					(254,18,0),
					(250,15,0),
					(245,11,0),
					(241,7,0),
					(236,3,0),
					(232,0,0),
					(227,0,0),
					(222,0,0),
					(218,0,0),
					(213,0,0),
					(209,0,0),
					(204,0,0),
					(200,0,0),
					(195,0,0),
					(191,0,0),
					(186,0,0),
					(182,0,0),
					(177,0,0),
					(172,0,0),
					(168,0,0),
					(163,0,0),
					(159,0,0),
					(154,0,0),
					(150,0,0),
					(145,0,0),
					(141,0,0),
					(136,0,0),
					(132,0,0),
					(127,0,0)]
				}

# to get a colour map from matplotlib:
#my_cm = matplotlib.cm.get_cmap('jet')
#test = numpy.arange(0,1,1.0/256)
#mapped = my_cm(test)
#mapped
#for c in mapped*255:
#    print("(%d,%d,%d)," % (int(c[0]), int(c[1]), int(c[2])))