import os
import pygame

import numpy
from libcolour import check_colour, colourmaps
from libcolour import colours as tangocolours

pygame.init()


class font_manager:
	
	def __init__(self):
		pass
	
	class FontProperties:
		
		def __init__(self, fname=None):
		
			if fname == None:
				fname = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Ubuntu-R.ttf')
			if os.path.isfile(fname):
				self.fname = fname
			else:
				raise Exception("ERROR in androidfriendly.matplotlib.font_manager.FontProperties: \
					font file does not exist '%s'" % fname)


class image:
	
	def __init__(self):
		
		pass
	
	
	def imread(self, filepath):
		
		img = pygame.image.load(filepath)
		w, h = img.get_size()
		outl = w*[[]]
		for x in range(w):
			outl[x] = h*[[]]
			for y in range(h):
				outl[x][y] = img.get_at((x,y))
		return numpy.array(outl)


class pyplot:
	
	def __init__(self):

		self._figlist = []

	
	def add_axes(self, axes):
		# TODO: not sure whether this should be implemented, as we are
		# currently using sub-Surfaces as the Axes, which already shares
		# its pixels with the figure Surface
		pass

	
	def close(self, fig):
		
		if fig == 'all':
			for f in self._figlist:
				f._close()
		elif type(fig) == int:
			f = self._figlist.pop(fig)
			self._close(fig)
		else:
			self._close(fig)

	
	def figure(self, figsize=(8.0, 6.0), dpi=100):
		
		# create a new figure
		newfig = self.Figure(figsize=figsize, dpi=dpi)
		
		# add to list
		self._figlist.append(newfig)
		
		return newfig
	
	
	def subplots(self, nrows=1, ncols=1, sharex=False, sharey=False, figsize=(8.0,6.0), dpi=100):
		
		fig = self.figure(figsize=figsize, dpi=dpi)
		if nrows == 1 and ncols == 1:
			return fig, self.Axes(fig, [0,0,1,1])
		ax = []
		w = 1.0 / ncols
		h = 1.0 / nrows
		for y in range(nrows):
			ax.append([])
			for x in range(ncols):
				ax[y].append(self.Axes(fig, [w*x, 1-h*y, w, h]))
		return fig, ax


	def _close(self, figure):
		
		del figure


	class Axes:
		
		def __init__(self, figure, rect):
			
			# create a new figure
			self.figure = figure
			fw, fh = self.figure.surf.get_size()
			self.rect = map(int, [rect[0]*fw, rect[1]*fh, rect[2]*fw, rect[3]*fh])
			self.surf = self.figure.surf.subsurface(self.rect)
			
			# list of colours we can use for plotting (ordered so that
			# successive colours are distinct)
			colournames = tangocolours.keys()
			colournames.remove("aluminium")
			self.colours = []
			for i in range(3):
				for cn in colournames:
					self.colours.append(tangocolours[cn][i])
			
			# list to contain information about plots
			self._plotlist = []
			
			# initialize font module (just to be sure)
			pygame.font.init()
		
		
		def annotate(self, s, pos, c=None, color=None, fontsize=12, fontproperties=None):
			
			# set colour
			if c == None and color == None:
				colour = (0,0,0)
			elif c == None and color != None:
				colour = color
			elif c != None and color == None:
				colour = c
			else:
				colour = (0,0,0)
			# initialize font
			if fontproperties == None:
				font = pygame.font.Font(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Ubuntu-R.ttf'), fontsize)
			else:
				font = pygame.font.Font(fontproperties.fname, fontsize)
			text = font.render(s, True, check_colour(colour))
			self.surf.blit(text, pos)

		
		def axis(self, dim):
			# dim can be [xmin, xmax, ymin, ymax] or 'off'
			pass

		
		def imshow(self, image, cmap=None, alpha=1, vmin=None, vmax=None):
			
			# load image from file
			if type(image) in [unicode, str]:
				if os.path.isfile(image):
					img = pygame.image.load(image)
				else:
					raise Exception("ERROR in androidfriendly.matplotlib.pyplot.Axes.imshow: \
						file '%s' does not exist!" % image)
			# copy existin Surface
			elif type(image) == pygame.Surface:
				img = image.copy()
			# assemble image from list
			elif type(image) in [list, numpy.Array]:
				w = len(image)
				h = len(image[0])
				image = ((image - numpy.min(image)) / numpy.max(image)) * 255
				img = pygame.Surface((w,h))
				for x in range(w):
					for y in range(y):
						if type(image[x][y]) in [int, float]:
							c = (image[x][y],image[x][y],image[x][y])
							img.fill(c, [x,y,1,1])
						else:
							img.fill(image[x][y], [x,y,1,1])
			# none of the above
			else:
				raise Exception("ERROR in androidfriendly.matplotlib.pyplot.Axes.imshow: \
					failed to load image (please pass a path to an \
					image file, a pygame.Surface instance, or a list \
					of lists resembling pixels)")
			# resize to Axes size
			newimg = pygame.transform.scale(img, self.rect)
			# set colour map
			if cmap != None:
				# check if the colourmap exists
				if cmap in colourmaps.keys():
					# loop through all pixels
					w, h = newimg.get_size()
					for x in range(w):
						for y in range(h):
							# get current colour
							c = newimg.get_at((x,y))
							# average over all pixels, and set
							# appropriate colour map colour
							c = numpy.mean(c[:3])
							newimg.set_at((x,y), (c,c,c,255))
				else:
					raise Exception("ERROR in androidfriendly.matplotlib.pyplot.Axes.imshow: \
						colour map '%s' not supported" % cmap)
			# scale everything below vmin back to vmin
			if vmin != None:
				# copy surface as it currently is
				ns = newimg.copy()
				# in the copy, colour everything to vmin
				ns.fill((vmin, vmin, vmin, 255))
				# in the copy, only copy only the pixels from the
				# that are not between 0 and vmin
				pygame.transform.threshold(ns, newimg, (vmin,vmin,vmin,255), (0,0,0,255), 2, None, False)
				# copy the copy back to the original
				newimg = ns.copy()
			# scale everything above vmin back to vmax
			if vmax != None:
				# copy surface as it currently is
				ns = newimg.copy()
				# in the copy, colour everything to vmin
				ns.fill((vmax, vmax, vmax, 255))
				# in the copy, only copy only the pixels from the
				# that are not between vmax and 255
				pygame.transform.threshold(ns, newimg, (255-vmax,255-vmax,255-vmax,255), (255,255,255,255), 2, None, False)
				# copy the copy back to the original
				newimg = ns.copy()
			# set alpha
			newimg.set_alpha(alpha)
			
			self.surf.blit(newimg, (0,0))
		
		
		def invert_xaxis(self):
			
			self.surf = pygame.transform.flip(self.surf, True, False)
			
		
		def invert_yaxis(self):
			
			self.surf = pygame.transform.flip(self.surf, False, True)
		
		
		def legend(self, loc='best', fontsize=12, fontproperties=None):
			
			# get legend location
			if type(loc) not in [str, unicode]:
				locs = {	0:'best',
						1:'upper right',
						2:'upper left',
						3:'lower left',
						4:'lower right',
						5:'right',
						6:'center left',
						7:'center right',
						8:'lower center',
						9:'upper center',
						10:'center'}
				loc = locs[loc]
			if loc == 'best':
				loc == 'upper right'
			# initialize font
			if fontproperties == None:
				font = pygame.font.Font(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Ubuntu-R.ttf'), fontsize)
			else:
				font = pygame.font.Font(fontproperties.fname, fontsize)
			# get plot info
			maxh = 0
			maxw = 0
			lbls = []
			for i in range(len(self._plotlist)):
				lbls.append(font.render(self._plotlist[i]['label'], True, (0,0,0,255)))
				w, h = lbls[-1].get_size()
				if w > maxw:
					maxw = w
				if h > maxh:
					maxh = h
			# get actual font position
			legpos = [0,0]
			if 'left' in loc:
				legpos[0] = 10
			elif 'right' in loc:
				legpos[0] = self.surf.get_width() - 10 - (maxw + 30)
			else:
				legpos[1] = self.surf.get_width()/2 - (maxw+30)/2
			if 'upper' in loc:
				legpos[1] = 10
			elif 'lower' in loc:
				legpos[1] = self.surf.get_height() - 10 - len(self._plotlist)*maxh
			else:
				legpos[1] = self.surf.get_height()/2 - (len(self._plotlist)*maxh)/2
			# draw rect
			self.surf.fill((255,255,255,255), [legpos[0],legpos[1], maxw+30, len(self._plotlist)*maxh+10])
			pygame.draw.rect(self.surf, (0,0,0,255), [legpos[0],legpos[1], maxw+30, len(self._plotlist)*maxh+10], 3)
			for i in range(len(self._plotlist)):
				# draw text
				self.surf.blit(lbls[i], (legpos[0]+30,legpos[1]+maxh/2+maxh*i))
				# draw line
				lpos = (legpos[0]+5, legpos[1]+10+maxh*i)
				rpos = (legpos[0]+25, legpos[1]+10+maxh*i)
				if '-' in self._plotlist[i]['markings']:
					pygame.draw.line(self.surf, self._plotlist[i]['colour'], lpos, rpos, 1)
				if 'o' in self._plotlist[i]['markings']:
					pygame.draw.circle(self.surf, (0,0,0,255), lpos, int(self._plotlist[i]['markersize']/2), 0)
					pygame.draw.circle(self.surf, self._plotlist[i]['colour'], lpos, int(self._plotlist[i]['markersize']/2 - self._plotlist[i]['markeredgewidth']), 0)
					pygame.draw.circle(self.surf, (0,0,0,255), rpos, int(self._plotlist[i]['markersize']/2), 0)
					pygame.draw.circle(self.surf, self._plotlist[i]['colour'], rpos, int(self._plotlist[i]['markersize']/2 - self._plotlist[i]['markeredgewidth']), 0)
				if 'x' in self._plotlist[i]['markings']:
					pygame.draw.line(self.surf, self._plotlist[i]['colour'], (lpos[0]-self._plotlist[i]['markersize']/2, lpos[1]-self._plotlist[i]['markersize']/2), (lpos[0]+self._plotlist[i]['markersize']/2, lpos[1]+self._plotlist[i]['markersize']/2), self._plotlist[i]['markeredgewidth'])
					pygame.draw.line(self.surf, self._plotlist[i]['colour'], (lpos[0]-self._plotlist[i]['markersize']/2, lpos[1]+self._plotlist[i]['markersize']/2), (lpos[0]+self._plotlist[i]['markersize']/2, lpos[1]-self._plotlist[i]['markersize']/2), self._plotlist[i]['markeredgewidth'])
					pygame.draw.line(self.surf, self._plotlist[i]['colour'], (rpos[0]-self._plotlist[i]['markersize']/2, rpos[1]-self._plotlist[i]['markersize']/2), (rpos[0]+self._plotlist[i]['markersize']/2, rpos[1]+self._plotlist[i]['markersize']/2), self._plotlist[i]['markeredgewidth'])
					pygame.draw.line(self.surf, self._plotlist[i]['colour'], (rpos[0]-self._plotlist[i]['markersize']/2, rpos[1]+self._plotlist[i]['markersize']/2), (rpos[0]+self._plotlist[i]['markersize']/2, rpos[1]-self._plotlist[i]['markersize']/2), self._plotlist[i]['markeredgewidth'])
		
		
		def plot(self, x, y, markings='o-', c=None, color=None, linewidth=1, markersize=5, markeredgewidth=1, alpha=1, label=None):
			
			if c == None:
				count = {}
				# go through all existing colours, and count how often
				# they occur in the current list of used colours
				for i in range(len(self.colours)):
					count[str(self.colours[i])] = 0
					for pi in range(len(self._plotlist)):
						if str(self._plotlist[pi]['colour']) not in count.keys():
							count[str(self._plotlist[pi]['colour'])] = 0
						count[str(self._plotlist[pi]['colour'])] += 1
				# get the colour with the lowest count
				c = count.keys()[0]
				for col in count.keys():
					if count[col] < count[c]:
						c = col
				# string to colour
				exec("c = %s" % c)
			else:
				c = check_colour(c)
			if len(c) == 1:
				c = (c, c, c)
			if len(c) == 3:
				c.append(255*alpha)
			# draw line
			for i in range(0, len(x)-1):
				spos = (x[i], y[i])
				epos = x[i+1], y[i+1]
				if '-' in markings:
					pygame.draw.line(self.surf, c, spos, epos, linewidth)
				if 'o' in markings:
					pygame.draw.circle(self.surf, (0,0,0,255*alpha), spos, int(markersize/2), 0)
					pygame.draw.circle(self.surf, c, spos, int(markersize/2 - markeredgewidth), 0)
				if 'x' in markings:
					pygame.draw.line(self.surf, c, (spos[0]-markersize/2, spos[1]-markersize/2), (spos[0]+markersize/2, spos[1]+markersize/2), markeredgewidth)
					pygame.draw.line(self.surf, c, (spos[0]-markersize/2, spos[1]+markersize/2), (spos[0]+markersize/2, spos[1]-markersize/2), markeredgewidth)
			if 'o' in markings:
				pygame.draw.circle(self.surf, (0,0,0,255*alpha), epos, int(markersize/2), 0)
				pygame.draw.circle(self.surf, c, epos, int(markersize/2 - markeredgewidth), 0)
			if 'x' in markings:
				pygame.draw.line(self.surf, c, (epos[0]-markersize/2, epos[1]-markersize/2), (epos[0]+markersize/2, epos[1]+markersize/2), markeredgewidth)
				pygame.draw.line(self.surf, c, (epos[0]-markersize/2, epos[1]+markersize/2), (epos[0]+markersize/2, epos[1]-markersize/2), markeredgewidth)
			# append info on line to list
			plotinfo = {	'label':label,
						'colour':c,
						'linewidth':linewidth,
						'markings':markings,
						'markersize':markersize,
						'markeredgewidth':markeredgewidth}
			self._plotlist.append(plotinfo)
			
		
		def set_axis_off(self):
			pass
		
		
		def set_title(self, title, fontproperties=None):
			pass
		
		
		def text(self, x, y, s, color=(0,0,0), fontsize=12, fontproperties=None):

			# NOTE: 	x is between 0 (left) and 1 (right)
			# 		y is between 0 (bottom) and 1 (top)
			pos = (int(x*self.surf.get_width()), int((1-y)*self.surf.get_height()))
			self.annotate(s, pos, c=color, fontsize=fontsize, fontproperties=fontproperties)
	
	
	class Figure:
		
		def __init__(self, figsize=(8.0, 6.0), dpi=100):
			
			# create a new Surface
			self.figsize = [float(figsize[0]), float(figsize[1])]
			self.dpi = dpi
			figsizepix = (int(self.figsize[0] * self.dpi), int(self.figsize[1] * self.dpi))
			self.surf = pygame.Surface(figsizepix)

		
		def savefig(self, filename):
			
			pygame.image.save(self.surf, filename)

		
		def set_dpi(self, dpi):
			
			self.dpi = dpi
			figsizepix = (int(self.figsize[0] * self.dpi), int(self.figsize[1] * self.dpi))
			self.surf = pygame.transform.scale(self.surf, figsizepix)

		
		def set_size_inches(self, figsize, forward=True):

			self.figsize = [float(figsize[0]), float(figsize[0])]
			figsizepix = (int(self.figsize[0] * self.dpi), int(self.figsize[1] * self.dpi))
			self.surf = pygame.transform.scale(self.surf, figsizepix)


# ready-instances (to spoof libraries)

font_manager = font_manager()
image = image()
pyplot = pyplot()

