#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 21:51:45 2020

@author: devyani
"""
import numpy as np
from numpy import loadtxt
import sys
input1 = sys.argv[1]
Xnew = loadtxt(str(input1), delimiter="\n")
output=[]
for i in range(len(Xnew)):
	#print(Xnew1[i])
  t=int(Xnew[i])
  if(t%3==0 and t%5==0):
    output.append('fizz buzz')
  elif(t%3==0 and t%5!=0):
    output.append('fizz')
  elif(t%5==0 and t%3!=0):
    output.append('buzz')
  else:
    output.append(int(Xnew[i]))
    
c = np.savetxt('output1.txt', output, delimiter =" ", fmt="%s")    
a = open("output1.txt", 'r')
