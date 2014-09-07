import os
import pygame


class font_manager:
	
	def __init__():
		pass
	
	def FontProperties():
		pass


class image:
	
	def __init__(self):
		
		pygame.init()
	
	
	def imread(filepath):
		
		return pygame.image.load(filepath)


class pyplot:
	
	def __init__(self):

		self._figlist = []

	
	def add_axes(axes):
		# TODO: not sure whether this should be implemented, as we are
		# currently using a sub-Surface as the Axes, which already shares
		# its pixels with the figure Surface
		pass

	
	def close(self, fig):
		
		if fig == 'all':
			for f in self._figlist:
				f._close()
		elif type(fig) == int:
			f = self._figlist.pop(fig)
			f._close()
		else:
			fig._close()

	
	def figure(self, figsize=(8.0, 6.0), dpi=100):
		
		# create a new figure
		newfig = self.Figure(figsize=figsize, dpi=dpi)
		
		# add to list
		self._figlist.append(newfig)
		
		return newfig
	
	
	def subplots(self, nrows=1, ncols=1, sharex=True, sharey=True):
		
		pass


	def _close(self, figure):
		
		del figure


	class Axes:
		
		def __init__(self, figure, rect):
			
			# create a new figure
			self.figure = figure
			fw, fh = self.figure.get_size()
			self.rect = rect[0]*fw, rect[1]*fh, rect[2]*fw, rect[3]*fh
			self.surf = figure.subsurface(self.rect)
			
			# list to contain information about plots
			self._plotlist = []
		
		
		def annotate(self, s, pos, fontsize=12, fontproperties=None):
			
			# TODO: render text; ignore properties?
			# text = 
			#self.surf.blit(text, pos)
			pass
		
		def axis(dim):
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
			elif type(image) == list:
				# TODO: something
				pass
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
				# TODO: something
				pass
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
		
		
		def legend(self, loc='best'):
			
			# TODO: while plotting, keep a list of labels and their line
			# colours and markers, so that we can create a legend here
			pass
		
		
		def plot(self, x, y, markings='o-', c=None, color=None, linewidth=1, markersize=5, markeredgewidth=1, alpha=1, label=None):
			
			# TODO: select colour (based on what's not in self._plotlist yet)
			# if c == None:
			#	select colour here
			if len(c) == 1:
				c = (c, c, c)
			if len(c) == 3:
				c.append(255*alpha)
			# draw line
			for i in range(len(x)-1):
				spos = (x[i], y[i])
				epos = x[i+1], y[i+1]
				if '-' in markings:
					pygame.draw.line(self.surf, c, spos, epos, linewidth)
				if 'o' in markings:
					pygame.draw.circle(self.surf, (0,0,0,255*alpha), spos, int(markersize/2), 0)
					pygame.draw.circle(self.surf, c, spos, int(markersize/2 - markeredgewidth), 0)
			# TODO: append info on line to list
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
			
			# NOTE: x is between 0 (left) and 1 (right),
			# y is between 0 (bottom) and 1 (top)
			pass
	
	
	class Figure:
		
		def __init__(self, figsize=8.0, dpi=100):
			
			# create a new Surface
			self.figsize = [float(figsize[0]), float(figsize[0])]
			self.dpi = dpi
			figsizepix = (int(self.figsize[0] * self.dpi), int(self.figsize[1] * self.dpi))
			self.surf = pygame.Surface(figsizepix)

		
		def savefig(self, filename):
			
			pygame.image.save(self.surf, filename)

		
		def set_dpi(self, dpi):
			
			self.dpi = dpi
			figsizepix = (int(self.figsize[0] * self.dpi), int(self.figsize[1] * self.dpi))
			self.surf = pygame.transform.scale(self.surf, figsizepix)

		
		def set_size_inches(self, figsize):

			self.figsize = [float(figsize[0]), float(figsize[0])]
			figsizepix = (int(self.figsize[0] * self.dpi), int(self.figsize[1] * self.dpi))
			self.surf = pygame.transform.scale(self.surf, figsizepix)
