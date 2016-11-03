#!/usr/bin/env python

from __future__ import division, print_function, absolute_import

import tflearn
from tflearn.layers.core import *
from tflearn.layers.conv import *
from tflearn.data_utils import *
from tflearn.layers.normalization import *
from tflearn.layers.estimator import regression
import h5py
import create_dataset

W = create_dataset.WIDTH
H = create_dataset.HEIGHT


def create_net():
    network = input_data(shape=[None, W, H, 3], dtype=tf.float32)
    network = conv_2d(network, W, 3, activation='relu')
    network = max_pool_2d(network, 2)
    network = conv_2d(network, W * 2, 3, activation='relu')
    network = conv_2d(network, W * 2, 3, activation='relu')
    network = max_pool_2d(network, 2)
    network = fully_connected(network, 1024, activation='relu')
    network = dropout(network, 0.5)
    network = fully_connected(network, 10, activation='softmax')
    network = regression(network, optimizer='adam',
                         loss='categorical_crossentropy',
                         learning_rate=0.001)
    return network

if __name__ == '__main__':
    h5f = h5py.File('data/bank.h5', 'r')
    X = h5f['X']
    Y = h5f['Y']

    net = create_net()
    model = tflearn.DNN(net, tensorboard_verbose=3)
    model.fit(X, Y, n_epoch=50, shuffle=True, show_metric=True, batch_size=1024)

    h5f.close()