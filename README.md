# Bachelor thesis: *Generating Structured Thermal Noise for Quantum Dynamical Systems*

Generation of colored structured noise for the simulation of energy fluctuations following non-Markovian correlations in quantum dynamical systems (light harvesting system). 

This is the code used for the generation of the data and plots of my bachelor thesis project at Jacobs University Bremen under the supervision of Prof. Ulrich Kleinekathöfer and Yannick Holtkamp.

## Abstract

To understand some of the most fundamental processes responsible for life on Earth, such as photosynthesis, quantum dynamical descriptions are of utmost importance. This analysis can be performed by studying the so-called open systems through a variation of the mean-field Ehrenfest Dynamics methods, known as Numerical Integration of Schr ̈odinger equation (NISE). A key ingredient for the calculations using NISE is the time-dependent site energies. Such fluctuations can be obtained from Molecular Dynamics (MD) simulations. However, these methods are usually computationally expensive, and do not provide the desired accuracy. An alternative approach is the generation of structured noise following the bath spectral density. This has been done previously for systems described by simple spectral functions.

In this thesis I implement an enveloping algorithm capable of generating noise with any arbitrary spectral density. Several tests are performed to verify the validity, scope and limitations of the algorithm. After finding the parameters necessary to replicate more complex spectral shapes, this noise is used in the calculation of population dynamics for a collection of test systems. These simulations provide insight on the parameter regimes and specific considerations for the implementation of the noise in these calculations, and yield useful information in the performance of NISE under the new frameworks.

![image](https://github.com/EmilianoG-byte/Quantum-Dynamics/assets/57567043/dd853656-0d49-4ba1-8231-66fbdacda957) ![Noise](https://github.com/EmilianoG-byte/Quantum-Dynamics/assets/57567043/82bde530-a9ca-4ab7-a4f6-131626d98272)  ![f2_20](https://github.com/EmilianoG-byte/Quantum-Dynamics/assets/57567043/10d4380c-c4fe-48a1-ad21-5f154fb84f91) ![f2_2](https://github.com/EmilianoG-byte/Quantum-Dynamics/assets/57567043/ae4fc942-385a-4545-9421-be84c6b7e37c)





## Structure

The `Notebooks` directory contains the ipynb files used for the generation of plots for the final report, as well as intermediate tests of spectral density functions (including comparisons with HEOM). The `Script` directory contains the python scripts with the main noise-generation algorithm, the generation of autocorrelation and spectral density functions, and the NISE algorithm sent to run in the server.

```
├── Notebooks
│   ├── Graphs-Generator.ipynb
│   ├── Lorentzian_modified.ipynb
│   ├── SD_tester.ipynb
├── Script
│   ├── Drude_Lorentzian_noise.pyb
│   ├── Lorentzian_noise_2peaks.py
│   ├── RunNise.py
│   ├── testing.py
├── .gitignore
└── README.md
```

## Report

See full report [here](https://emilianog-byte.github.io/projects/2_BachelorThesis/).
