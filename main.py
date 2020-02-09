#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 18:55:05 2020

@author: devyani
"""
import numpy as np
from numpy import loadtxt
from tensorflow.keras.models import load_model
import tensorflow as tf
from tensorflow.python import keras
import sys




def change_to_binaryarray(binary_string):
  binary_string=str(binary_string)
  num_of_zeros=10-len(binary_string)
  binary_string=('0'*num_of_zeros)+binary_string
  binary_array=list(binary_string)
  #print(l)
  return binary_array


model = load_model('fizzbuzzmodel.h5')

input1 = sys.argv[1]+'.txt'
print(input1)
# summarize model.
#model.summary()
Xnew = loadtxt(str(input1), delimiter="\n")
Xnew1 = loadtxt(str(input1), delimiter="\n")
#print(dataset)

Mnew=np.zeros([len(Xnew),10])

 #convert X to binary string 
for i in range(Xnew.shape[0]):
          Xnew[i]='{0:08b}'.format(int(Xnew[i]))


for i in range(Xnew.shape[0]):
          Mnew[i]=change_to_binaryarray(int(Xnew[i]))


ynew = model.predict_classes(Mnew)
output=[]
#print(Mnew)
# show the inputs and predicted outputs
for i in range(len(Xnew)):
	#print(Xnew1[i])
  t=ynew[i]
  if(t==0):
    output.append('fizz buzz')
  elif(t==1):
    output.append('fizz')
  elif(t==2):
    output.append('buzz')
  else:
    output.append(int(Xnew1[i]))


c = np.savetxt('Software2.txt', output, delimiter =" ", fmt="%s")    
#a = open("Software2.txt", 'r')# open file in read mode 
  

output1=[]
for i in range(len(Xnew1)):
	#print(Xnew1[i])
  t=int(Xnew1[i])
  if(t%3==0 and t%5==0):
    output1.append('fizz buzz')
  elif(t%3==0 and t%5!=0):
    output1.append('fizz')
  elif(t%5==0 and t%3!=0):
    output1.append('buzz')
  else:
    output1.append(int(Xnew1[i]))
    
print(len(output1),len(output))
c = np.savetxt('Software1.txt', output1, delimiter =" ", fmt="%s")    
a = open("Software1.txt", 'r')
