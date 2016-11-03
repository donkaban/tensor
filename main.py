#!/usr/bin/env python


import tflearn
from tflearn.layers.core import *
from tflearn.layers.conv import *
from tflearn.data_utils import *
from tflearn.layers.normalization import *
from tflearn.layers.estimator import regression

# CIFAR-10 Dataset
from tflearn.datasets import cifar10

(X, Y), (X_test, Y_test) = cifar10.load_data()
Y = to_categorical(Y, 10)
Y_test = to_categorical(Y_test, 10)

# Create a hdf5 dataset from CIFAR-10 numpy array
import h5py
h5f = h5py.File('data.h5', 'w')
h5f.create_dataset('cifar10_X', data=X)
h5f.create_dataset('cifar10_Y', data=Y)
h5f.create_dataset('cifar10_X_test', data=X_test)
h5f.create_dataset('cifar10_Y_test', data=Y_test)
h5f.close()
