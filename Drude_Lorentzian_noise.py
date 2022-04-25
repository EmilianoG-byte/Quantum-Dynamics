# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 23:23:21 2021

@author: emili
"""
from pylab import * #importing several functions from pylab, including numpy and pyplot

import numpy as np
import math
from math import pi
from numpy.lib import scimath as SM

def noise_algorithm(total_time,reals,site,dt,gamma,strength_cm,Sko,Wko,Gammak):#this contains the noise generation algorithm
    #Constants over the whole procedure
    k = 8.6173303E-5 #boltzmann constant in eV/K
    T = 300 #Temperature in K
    hbar = 0.658211951 # in eV-fs
    N = (int(total_time/dt)+1) #+1 to account for the dt/dt that we need if  we want to have our time and Noise exactly finish at total_time
    
    #Drudian
    gamma = gamma*1.23984*10**(-4)/(hbar) #converting the gamma given in cm to rad/fs
    strength = 1.23984E-4 *strength_cm #converting the strength from cm to eV
    
    #Lorentzian
    Sk = array(Sko) # before was array([Sk]), now Sk and Wk need to be passed already as [] since I want to pass it on RunNise code
    Wk = array(Wko)*1.23984*10**(-4)/hbar #converting to array and to rad/fs
    Gammak =  Gammak*1.23984*10**(-4)/(hbar) #converting the gamma given in cm to rad/fs
    
    def spectral(w): #drude + lorentzian spectral density
        S = 0
        for i in range(len(Wk)):
            S += hbar*4*k*T*Sk[i]*Wk[i]**3*Gammak/((Wk[i]**2-w**2)**2+(w**2*Gammak**2))
            #Recall S(w) =/ J(w)
        return S + 4*gamma*strength*k*T/((w**2+gamma**2))

    def generate_noise(mean, var,N,reals,site,dt):
        white_noise = np.random.normal(mean, var, size=(reals*site,N)) #generates matrix with white noise. Shape = reals x N. Here, mean = 0 and var = 1
        freq = np.fft.fft(white_noise)*1/sqrt(dt) #fourier transform of the white noise: W
        freq_bins = np.fft.fftfreq(N,dt)*2*pi #frequencies associated to fft(white noise)
        freq_enveloped = SM.sqrt(spectral(freq_bins)) * freq #sqrt(S)*W
        return np.real(np.fft.ifft(freq_enveloped))
    
    OldNoise = generate_noise(0, 1, N, reals,site,dt)
    
    print(shape(OldNoise)) #returns noise matrix of size (reals x N). N:= (length/dt + 1)*site
    
    NewNoise = np.zeros((reals,N,site))#NEmpty 3D array with correct dimensions
                                        # first dimension: realizations
                                        # second dimension: total_time + 1
                                        # third dimension: number of sites
    print(shape(NewNoise))
    
    for j in range(0,site):
        print(j)
        #NewNoise[:,:,j] = OldNoise[:,j*N2:(j+1)*N2] #assigning to each site N2 elements := total_time/dt + 1
        NewNoise[:,:,j] = OldNoise[j*reals:(j+1)*reals,0:N]
        print(shape(NewNoise[:,:,j]))
    
    print('Finished algorithm properly')
    return NewNoise


def main():
    print('You are using this script as your main')
    
if __name__=='__main__':
    main()