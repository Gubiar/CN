#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 15:49:09 2020

@author: Gubiar
"""

def f(x):
    
   print("teste")
    
   a = -4 + 8*x - 5 * pow(x,2) + pow(x,3)
   return a

def bisseccao(f,xi,xs,itmax,ea):
    
    it=0;
    
    while (it<= itmax and abs((f(xi)*f(xs)))>ea):
        print('teste1')
        it=it+1
        Xn=(xi + xs)/2
        
        if(f(Xn)*f(xi)<0):
            xs=Xn
        else:
            xi = Xn
            
    
    return xi,it

print(bisseccao(f,1/2,3,1000,10e-20))
    
