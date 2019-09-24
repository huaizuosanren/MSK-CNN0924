import matplotlib.pyplot as plt
import numpy as np
np.random.seed(1337)  # for reproducibility

from math import pi
from scipy import interpolate 
import matplotlib.pyplot as plt
import matplotlib
import scipy.signal as signal
import math
import cmath

def symbol_out(data_len):
	a=np.random.randint(0, 2, data_len)
	a=1-2*a
	return a

def modulate(x,data_len,sample_num):
	y= np.zeros(data_len*sample_num)
	yy=np.zeros(data_len*sample_num,dtype = complex)
	print(x)
	if x[0]>=0:
		y[0:sample_num]=np.arange(pi/2/sample_num,pi/2+pi/2/sample_num,pi/2/sample_num)
	else:
		y[0:sample_num]=-np.arange(pi/2/sample_num,pi/2+pi/2/sample_num,pi/2/sample_num)
	for ii in range(1,len(x)):
		if x[ii]>=0:
			y[(ii*sample_num):(ii+1)*sample_num]=y[(ii)*sample_num-1]+np.arange(pi/2/sample_num,pi/2+pi/2/sample_num,pi/2/sample_num)
		else:
			y[(ii*sample_num):(ii+1)*sample_num]=y[(ii)*sample_num-1]-np.arange(pi/2/sample_num,pi/2+pi/2/sample_num,pi/2/sample_num)
	print (y)
	for i in range(0,len(y)):
		#y[i]=y[i]%(2*pi)
		#print(y[i])
		yy[i]=complex(np.cos(y[i]),np.sin(y[i]))
	#fig = plt.figure() 
	#plt.plot(y, 'b')
	return yy
