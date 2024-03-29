import matplotlib.pyplot as plt
import numpy as np
from math import pi
import matplotlib.pyplot as plt
import matplotlib
import scipy.signal as signal
import math
#import numpy as np
import tensorflow as tf
from keras import backend as K
from scipy.stats import levy_stable

 
def awgn(y, snr):
 
    snr = 10 ** (snr / 10.0)
    xpower = np.sum(y ** 2) / len(y)
    npower = xpower / snr
    return np.random.randn(len(y)) * np.sqrt(npower) + y

def CalScale(GSNR,alpha,R):
    '''
    To calculate the parameter - scale from given alpha and GSNR
    according to Symmertic Alpha-Stable Distribution
    :param GSNR: Geometry SNR
    :param alpha: Characteristic exponent
    :param R: Code Rate
    :return: scale parameter - gamma
    '''
    GSNR = 10 ** (GSNR / 10)  # Eb/No conversion from dB to decimal
    S0 = 1 / (np.sqrt(7.12 * GSNR * R))
    gamma = ((1.78 * S0) ** alpha) / 1.78
    scale = gamma ** (1 / alpha)
    return scale

def Inoise(alpha_train,x1,x2,x3):
    y = np.float32(levy_stable.rvs(alpha_train,0,x1,x2,x3))
    return y

def addNoise(x,sigma,alpha_train):
    '''
    Add noise (Gaussian and Impulsive)
    :param x:
    :param sigma:
    :return:
    '''
    w=tf.py_func(Inoise,[alpha_train,0,sigma,K.shape(x)],tf.float32)
    w.set_shape(x.get_shape())
    return x + w

if __name__ == '__main__':
    ## Check the calculation and result
    alpha_train=2
    R=1/2
    GSNR=1
    scale=CalScale(GSNR,alpha_train,R)
    print(scale)