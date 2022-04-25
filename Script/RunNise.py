import NisePytorchMulticoreNsite as Nise
import numpy as np
import torch
import matplotlib.pyplot as plt
#from colored_noise_like_fortran import noise,multi_noise
#from Lorentzian_noise import noise_algorithm
#from Drude_noise import noise_algorithm
#from Lorentzian_noise_2peaks import noise_algorithm 
from Drude_Lorentzian_noise import noise_algorithm 

model = Nise.Net()

dw0=0 #does not matter here 
V=0 #does not matter here
T=300 #also does not matter. The actual T is included in the noise_algorithm
Er=37 #Reorganization energy (Lambda)

cortim=30 #does not really matter when not using it in noise

gamma = 30 #in cm-1

total_time= 20000 #fs
step=1 #fs
reps=2000 #realizations
psi0=0 #does not matter here
M=2 #sites
factor = (1.23984E-4) #multiply by factor to convert ev--->cm-1



#array with all the frequencies and S
"""S_all = np.array([0.011, 0.011, 0.009, 0.009, 0.010, 0.011, 0.011, 0.012, 0.003, 0.008,
         0.008, 0.003, 0.006,  0.002, 0.002, 0.002,  0.001, 0.002, 0.004,  0.007, 
         0.004, 0.004, 0.003,  0.006, 0.004, 0.003, 0.007, 0.010, 0.005, 0.004, 
         0.009, 0.018,  0.007, 0.006, 0.007, 0.003, 0.004, 0.001,  0.001,  0.002, 
         0.002,  0.003, 0.001, 0.002, 0.002, 0.001, 0.001, 0.003, 0.003, 0.009, 0.007,
         0.010, 0.003, 0.005, 0.002, 0.004, 0.007, 0.002, 0.004, 0.002, 0.003, 0.003])
        #array with all wk
W_all = np.array([46, 68, 117, 167, 180, 191, 202, 243, 263, 284, 291, 327, 366, 385, 404, 423, 440, 
         481, 541, 568, 582, 597, 630, 638, 665, 684, 713, 726, 731, 750, 761, 770, 795, 821,
         856, 891, 900, 924, 929, 946, 966, 984, 1004, 1037, 1058, 1094, 1104, 1123, 1130, 1162,
         1175, 1181, 1201, 1220, 1283, 1292, 1348, 1367, 1386, 1431, 1503, 1545])"""

S_all = [0.02396,  0.02881, 0.03002, 0.02669,  0.02669, 0.06035, 0.02487, 0.01486, 
          0.03942, 0.00269, 0.00849, 0.00303,  0.00194,  0.00197, 0.00394, 0.03942,
          0.02578, 0.00485, 0.02123,  0.01031, 0.02274, 0.01213, 0.00636, 0.01122, 
          0.04094,  0.01759, 0.00667, 0.01850,  0.01759, 0.00697, 0.00636, 0.00636, 
          0.00454, 0.00576, 0.03032, 0.00394, 0.00576, 0.00667, 0.00667, 0.00788, 
          0.00636, 0.02183, 0.00909, 0.00454, 0.00454, 0.00454, 0.00363, 0.00097]

W_all = [97, 138, 213, 260, 298, 342, 388, 425, 518, 546, 573, 585, 604, 700, 
     722, 742,752, 795, 916, 986, 995, 1052, 1069, 1110, 1143, 1181, 1190, 
     1208, 1216, 1235, 1252, 1260, 1286, 1304, 1322, 1338, 1354, 1382, 1439,
     1487, 1524, 1537, 1553, 1573, 1580, 1612, 1645, 1673]

gammak = 7 #in cm-1


#Sk and Wk for the lorentzian. Testing each of them
#Sk = [0.0090,0.008,0.008]
#Wk = [117,284,291]

#Reminder: What I have in my Ntbk is not index but number of peak
f = 1
index = 4
#index2 = 1
#index3 = 2
#Sk = [S_all[index]*f,S_all[index2],S_all[index3]] #multiplying by factor to see if this creates differences
#Wk = [W_all[index],W_all[index2],W_all[index3]]

Sk = [S_all[index]*f] #multiplying by factor to see if this creates differences
Wk = [W_all[index]]

#Sk = [0.01]
#Wk = [260]


Hfull=np.zeros((reps,int((total_time+step)/step),M,M))
#Hfull+= np.array([[10,-87.7,5.5,-5.9],[-87.7,130,30.8,8.2],[5.5,30.8,-190,-53.5],[-5.9,8.2,-53.5,-80]])
Hfull+=np.array([[0,100],[100,0]]) #Used to compare with Hannes. Only two peaks

#Dividing by factor in both Drude and Lorentzian to obtain results in cm-1 and not eV
#mynoise=noise_algorithm(total_time,reps,M,step)/factor #for lorentzian
#mynoise=noise_algorithm(total_time,reps,M,step,cortim,Er)/factor #for Drude
#mynoise=noise_algorithm(total_time,reps,M,step,Sk,Wk)/factor #for lorentzian for two peaks

mynoise=noise_algorithm(total_time,reps,M,step,gamma,Er,Sk,Wk,gammak)/factor #Drude + Lorentzian 

#mynoise=mynoise[:,0:int((total_time+step)/step),:] #if I want to try this one again I need to use 2*total_time on my_noise, previous line

#mynoise=np.load("noise.npy")  #### 3 dimensions first dimension: realizations 2nd dimension time third dimension site
                              #### for each site calculate noise with int((total_time+step)/step) (maybe your N) timesteps and number of realizations (100)
                              ### mynoise = np.zeros(reps,int((total_time+step)/step),NumSites) #Numsites is number of sites
                              ### noise1 int((total_time+step)/step) timesteps reps realizations mynoise[:,:,0]=noise1
                              ### noise2 int((total_time+step)/step) timesteps reps realizations mynoise[:,:,1]=noise2 etc
                              ### np.save(mynoise,"noise.npy")
#np.save('Fluctuation_1000',mynoise)                              
Hfull=torch.tensor(Hfull,dtype=torch.float)                              
for i in range(0,M):
    Hfull[:,:,i,i]+=mynoise[:,:,i]
    
"""mynoise=multi_noise((reps,M,int((total_time+step)/step)),step,T,cortim,Er)
#np.save('Tests_Y1000',mynoise)
Hfull=torch.tensor(Hfull,dtype=torch.float)
for i in range(0,M):
    Hfull[:,:,i,i]+=mynoise[:,i,:]"""




res,diff_t,totres=model.simulate(dw0, V,T,Er,cortim,total_time,step,reps,psi0,Hfull,device="cpu",T_correction="None")

#np.save("sayandiff.npy",res)
#np.save("testing4.npy",totres)
for i in range(0,1):
    plt.plot(totres[:,i],label="site "+str(i+1))

#plt.title("Lorentzian $W_k = {0} 1/cm $ and T = {1} fs".format(Wk,total_time))
#plt.title("Population Dynamics: $\lambda =$ {0}, $\gamma = $1/{1}".format(Er,cortim))
#plt.title("Noise from Enveloping Algorithm, index: {0}, W_k: {1} ".format(index, W_all[index]))
plt.title("$\lambda = $ {0}, $\gamma = $ {1}, $\lambda_k = $ {2} ".format(Er,gamma,S_all[index]*W_all[index]))
#plt.title("$\lambda = $ {0}, $\gamma = $ {1}, indices: {2} and {3} and {4} ".format(Er,gamma,index,index2, index3))
#plt.title("Yannick's Drude Er = 10 $cm^{-1}$")
plt.xlabel("time [fs]")
plt.ylabel("population")
plt.xlim(-100,5000)
#np.save("sayandiff_C.npy",diff_t)
#plt.plot(diff_t,label="diff")
plt.legend()
print(res)
