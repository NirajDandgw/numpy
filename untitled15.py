# -*- coding: utf-8 -*-
"""Untitled15.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FlkCBHvSc6w5BYkxJfFdPGSXdwBtqHap
"""

import numpy as np
arr=np.array([1,2,3,4,5])
arr

list_of_list=[[1,2,3],[4,5,6],[6,7,8]]
np.array(list_of_list)

np.arange(1,19)

np.arange(1,45,5)

np.zeros(10)

np.zeros(10,int)

np.zeros(10,dtype=int)

np.ones(10)

np.ones((2,10))

np.zeros((2,4))

np.linspace(0,20,6)#equel dividing by number start by zero and second is number that duviding and last is number of times is dividing

np.eye(4)#identity matrix

np.random.rand(3,2)#uniformly distrubuted by range 0 to 1 any random num

np.random.randn(3,2)#randn negative num also include

np.random.randint(10,100)#it give random num from range 10 to 100

np.random.randint(34,56,100)#it give 100 random num from range 34 to 56

sample_array=np.arange(30)
sample_array

rand_array=np.random.randint(0,100,20)
rand_array

sample_array.reshape(6,5)

rand_array.min()#get minimun value in rand_array

rand_array.argmin()#it give index of the minimum num

rand_array.max()

rand_array.argmax()

sample_array.dtype

a=np.eye(5)
a

a.T

import numpy as np
sample_arra=np.arange(10,30)
sample_arra

sample_matrix=np.array(([1,2,3],[4,5,6],[85,45,6]))
sample_matrix

sample_matrix[0][2]

sample_matrix[2,:]

sample_matrix[2]

sample_matrix[:,(1,2)]

#selection tecnique
sample_array=np.arange(1,20)
sample_array

sample_array+sample_array

np.exp(sample_array)

np.sqrt(sample_array)

np.log(sample_array)

np.max(sample_array)

np.min(sample_array)

np.argmax(sample_array)

np.square(sample_array)

np.std(sample_array)

np.var(sample_array)

np.mean(sample_array)

array=np.random.randn(1,4)
array

np.round(array,decimals=1)

sports=np.array(['golf','cricket','football','football','cricket'])
np.unique(sports)

#



