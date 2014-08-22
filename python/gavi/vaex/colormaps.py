# -*- coding: utf-8 -*-
import matplotlib.cm
import numpy as np
cols = []
for x in np.linspace(0,1, 256):
	rcol = 0.237 - 2.13*x + 26.92*x**2 - 65.5*x**3 + 63.5*x**4 - 22.36*x**5
	gcol = ((0.572 + 1.524*x - 1.811*x**2)/(1 - 0.291*x + 0.1574*x**2))**2
	bcol = 1/(1.579 - 4.03*x + 12.92*x**2 - 31.4*x**3 + 48.6*x**4 - 23.36*x**5)
	cols.append((rcol, gcol, bcol))

name = 'PaulT_plusmin'
cm_plusmin = matplotlib.colors.LinearSegmentedColormap.from_list(name, cols)
matplotlib.cm.register_cmap(name=name, cmap=cm_plusmin)

colormaps = []
cmaps = [	('Extra', ['PaulT_plusmin']),
				('Sequential',     ['binary', 'Blues', 'BuGn', 'BuPu', 'gist_yarg',
								'GnBu', 'Greens', 'Greys', 'Oranges', 'OrRd',
								'PuBu', 'PuBuGn', 'PuRd', 'Purples', 'RdPu',
								'Reds', 'YlGn', 'YlGnBu', 'YlOrBr', 'YlOrRd']),
			('Sequential (2)', ['afmhot', 'autumn', 'bone', 'cool', 'copper',
								'gist_gray', 'gist_heat', 'gray', 'hot', 'pink',
								'spring', 'summer', 'winter']),
			('Diverging',      ['BrBG', 'bwr', 'coolwarm', 'PiYG', 'PRGn', 'PuOr',
								'RdBu', 'RdGy', 'RdYlBu', 'RdYlGn', 'seismic']),
			('Qualitative',    ['Accent', 'Dark2', 'hsv', 'Paired', 'Pastel1',
								'Pastel2', 'Set1', 'Set2', 'Set3', 'spectral']),
			('Miscellaneous',  ['gist_earth', 'gist_ncar', 'gist_rainbow',
								'gist_stern', 'jet', 'brg', 'CMRmap', 'cubehelix',
								'gnuplot', 'gnuplot2', 'ocean', 'rainbow',
								'terrain', 'flag', 'prism'])]
for cmap_category, cmap_list in cmaps:
	for colormap_name in cmap_list:
		colormaps.append(colormap_name)