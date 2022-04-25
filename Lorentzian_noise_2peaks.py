from pylab import * #importing several functions from pylab, including numpy and pyplot
import numpy as np
import math
from math import pi
from numpy.lib import scimath as SM #used for the square root of the enveloping section of algorithm

def noise_algorithm(total_time,reals,site,dt,Sko,Wko):
    #Constants over the whole procedure
    k = 8.6173303E-5 #boltzmann constant in eV/K
    T = 300 #Temperature in K
    hbar = 0.658211951 # in eV-fs
    #N = (int(total_time/dt)+1)*site #+1 to account for the dt/dt that we need if  we want to have our time and Noise exactly finish at total_time
    N = (int(total_time/dt)+1)
    Gammak =  0.00062/hbar #9.4196*10**(-4) #rad/fs
    
    
    
    
    
    #array with all the frequencies and S
    Sk = array(Sko) #only for the first peak #27th April: before was array([Sk]), now Sk and Wk need to be passed already as [] since I want to pass it on RunNise code
    #Sk = array([0.007, 0.018])
    #Wk = array([568, 770])*1.23984*10**(-4)/hbar
    Wk = array(Wko)*1.23984*10**(-4)/hbar #only for the first peak

    
    
    #this contains the noise generation algorithm
    def spectral(w): #drude spectral density
        #converting the frequencies to angular frequencies. Update: done already on the definition as requested by professor        
        S = 0
        for i in range(len(Wk)):
            S += hbar*4*k*T*Sk[i]*Wk[i]**3*Gammak/((Wk[i]**2-w**2)**2+(w**2*Gammak**2))
        return S

    def generate_noise(mean, var,N,reals,site,dt):
        white_noise = np.random.normal(mean, var, size=(reals*site,N)) #generates matrix with white noise. Shape = reals x N. Here, mean = 0 and var = 1
        freq = np.fft.fft(white_noise)*1/sqrt(dt) #fourier transform of the white noise: W
        freq_bins = np.fft.fftfreq(N,dt)*2*pi #frequencies associated to fft(white noise)
        freq_enveloped = SM.sqrt(spectral(freq_bins)) * freq #sqrt(S)*W
        return np.real(np.fft.ifft(freq_enveloped))
    
    OldNoise = generate_noise(0, 1, N, reals,site,dt)
    
    print(shape(OldNoise)) #returns noise matrix of size (reals x N). N:= (length/dt + 1)*site

    #N2 = int(total_time/dt)+1  #15th April: basically here is N because 1st axis is the longer one
    
    NewNoise = np.zeros((reals,N,site))#NEmpty 3D array with correct dimensions
                                        # first dimension: realizations
                                        # second dimension: total_time + 1
                                        # third dimension: number of sites
    print(shape(NewNoise))
    
    for j in range(0,site):
        print(j)
        #NewNoise[:,:,j//2] = OldNoise[:,j*N2:(j+1)*N2] #assigning to each site N2 elements := total_time/dt + 1
        #NewNoise[:,:,j//2] = OldNoise[j*reals:(j+1)*reals,0:N2] #taking only alternating blocks: Y,N
        NewNoise[:,:,j] = OldNoise[j*reals:(j+1)*reals,0:N]
        print(shape(NewNoise[:,:,j]))
    #assigning the noise values to each site
    #Explanation: for each site j we are going from the j*Nth element to the (j+1)*Nth element. 
    #Recall: for slicing the last element is not taken into account. Example, site = 4, N = 101, reals= 100:
    #j = 1: 0-->100, 101-->201, 202-->302, 303-->403. Each of them has N elements. 404th element is called by 403.
    
    print('Finished algorithm properly')
    return NewNoise
        
        
        
def main():
    print('You are using this script as your main')
    
if __name__=='__main__':
    main()