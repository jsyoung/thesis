'''
This is a simple script which can be imported to the effect of 
compressing and streamlining other import operations for analysis
into a single simple 

from thesis.tools.bundle import *

Won't be fast, but it should be complete.
'''
import logging
logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s: %(levelname)s: %(message)s',
    datefmt='%m/%d/%Y %H:%M:%S')

logging.info('Execution Initiated')
import matplotlib
matplotlib.use('Agg')
import os

# import the whole of numpy, it will be used everywhere.
import numpy as np
from scipy.io.netcdf import netcdf_file as nc
import os, sys, time
from pylab import *
from scipy import *
from . import *
from mymap import *
# the sources library was implemented
# in a non-standard way for various reasons
# #import thesis.analysis.sources as srcs
try:
    import thesissources as srcs
    s = srcs
    sources = srcs
except:
    logging.warning('You have no installed sources package, that might cause problems. "srcs" namespace not available')
import matplotlib.pyplot as plt
from core.pytables import h5
from core.objects import CoreObject as co
import figure as TFigure
from figure import *
from sounding import *
from metcalcs import *
import cleanfig
from cleanfig import *

# Analysis methods
from   thesis.analysis import *
from   thesis.analysis.pcaps import *
import thesis.analysis.lidar.mlh as mlh
from   thesis.analysis.lidar.particle import *
from   thesis.analysis.lidar.ceil import Filter

from matplotlib.backends.backend_pdf import PdfPages
import mymap as mymap
import tables


logging.info(__name__ + ' imported')
