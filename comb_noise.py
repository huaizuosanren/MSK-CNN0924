'''
--------it was tested on jupyter and successed on 2019/03/29------------------
'''
import matplotlib.pyplot as plt
import numpy as np 
from math import pi
from scipy import interpolate 
import matplotlib.pyplot as plt
import matplotlib
import scipy.signal as signal
import math
from scipy.stats import levy_stable
import CommFunc as CF

def combnoise(snr_db,yita,length,fc,fs):
	snr = 10**(snr_db/10)
	#Ptotal = 0.5/snr
	Ptotal = 1/snr
	#P_im = Ptotal*yita
	P_comb = Ptotal*(1-yita)
	ts = np.arange(1/fs, (length+1) / fs, 1 / fs)
	#comb_noise = (P_comb**0.5)*np.random.randn(length)*np.cos(np.dot(2*pi*fc,ts))
	comb_noise =  (P_comb**0.5)*np.random.random(length)*np.cos(np.dot(2*pi*fc,ts))- (P_comb**0.5)*np.random.random(length)*np.sin(np.dot(2*pi*fc,ts))
	return comb_noise

def noise(input_shape,alpha=1.5,beta=0,scale=1):
    im_noise=levy_stable.rvs(alpha,beta,0,scale,input_shape)
    return im_noise

def imnoise(snr_db,yita,input_shape,alpha=1.5):
	#GSNR = snr_db*2  #
	GSNR = snr_db+3
	#alpha = 1.5
	beta = 0
	R=1
	scale=CF.CalScale(GSNR,alpha,R)
	scale2 = scale*yita
	#im_noise= yita*noise(input_shape,alpha,beta,scale)
	im_noise= noise(input_shape,alpha,beta,scale2)
	return im_noise

def combinenoise(snr_db,yita,length,input_shape,fc,fs):
	im_noise = imnoise(snr_db,yita,input_shape)
	comb_noise = combnoise(snr_db,yita,length,fc,fs)
	combine_noise = im_noise + comb_noise
	return combine_noise

comb_noise=combnoise(2,0.2,1000,20000,200000)
im_noise=imnoise(2,0.2,[1,1000])
combine=comb_noise+im_noise
combine
#----需要注意一件事：生成的数组名不能和函数名是一个，否则python会乱，不知道这个名字是数组还是调用的函数，就会报错-----------