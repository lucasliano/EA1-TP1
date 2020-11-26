# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 15:26:08 2020

Este algoritmo permite graficar con escala logaritmica simple un grafico compuesto por varios arrays.



@author: LucasLiaño
"""

import matplotlib.pyplot as plt

w = [
     20,
     50,
     100,
     500,
     1000,
     10000,
     20000,
     50000,
     75000,
     100000,
     ]

valores1uf = [
    0.493,
    0.769,
    0.862,
    0.900,
    0.901,
    0.901,
    0.901,
    0.896,
    0.889,
    0.880
    ]


valores10uf = [
    0.891,    
    0.900,    
    0.901,  
    0.901,
    0.901, 
    0.901,
    0.901,
    0.896,
    0.889,
    0.880
    ]  
    
    
fig = plt.figure(1)
axs = fig.add_subplot(1, 1, 1)
plt.xscale('symlog')
axs.set_title("MMBFU310LT1")



axs.plot(w,valores10uf, '*-g',  label="$10 \mu F$")
axs.plot(w,valores1uf,  'x--m',  label="$1 \mu F$" )

axs.set_xlabel('$\omega$ [Hz]')  
axs.set_ylabel('$A_{VS}(\omega)$')  
axs.set_xlim(10,150000)
axs.set_ylim(0.4,1)
axs.legend()
axs.grid() 
    
    
    
    
    
    
    
    
    
    