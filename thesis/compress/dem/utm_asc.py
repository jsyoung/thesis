"""
	A non-standard importable processor for ASCII Digital Elevation Models of the format
	provided by sebastian, in UTM coordinates. 

	These files contain no actually referensible information as to precise earthly location, be warned...

"""

import numpy as np
from thesis.tools.pytables import *


def read(src,save=False):
	"""
		this function can now create an hdf5 archive of this data
	"""
	print "Reading",src
	f = open(src,'r')

	# now set a variable wich will then be contoured

	d = False
	x = False
	y = False
	stats = {}

	curr_y = 0
	nan = float('nan')
	x_set = False
	print 'reading!'
	for line in f:
		if len(line) < 100:
			print line
			p = line.split()
			# record the information
			stats[p[0]] = float(p[1])
			continue
		if type(d) == bool:
			# then it is time to set d
			x = np.arange(stats['xllcorner'],stats['ncols']*stats['cellsize']+stats['xllcorner'],stats['cellsize'])
			y = np.arange(stats['nrows']*stats['cellsize']+stats['yllcorner'],stats['yllcorner'],-1*stats['cellsize'])
			d = np.zeros((stats['nrows'],stats['ncols']),dtype=np.float)
			if save:
				print x
				doc = h5(save)
				# make the hdf5 document - scary huge at first, but it will be ok.
				doc.create(x=int(stats['ncols']),y=int(stats['nrows']),topo=[stats['nrows'],stats['ncols']])

		curr_x = 0
		#y.append(curr_y)# append the current y index, since we will only go through it once
		# well, this is a data line, each box is def
		d[curr_y] = np.fromstring(line.replace(str(stats['nodata_value'])+"0",'nan'),sep=" ") #FIXME - '0' is bad
		"""
		for k in line.split():
			
			curr_x += 1
			# fill in the values of x if there are not any saved
			#if not x_set:
			#	x.append(curr_x)
	
			if float(k) == stats['nodata_value']:
				d[curr_y,curr_x-1] = nan
				continue
	
			# well, save the value,
			d[curr_y,curr_x-1] = float(k)
		"""
		# now we need to 
		# well, x should have been set at this point
		curr_y += 1
		x_set = True
	if save:
		doc.append(0,x=x,y=y,topo=d) #and that is that!
		return True
	return x,y,d

