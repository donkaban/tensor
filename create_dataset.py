#!/usr/bin/env python

from __future__ import division, print_function, absolute_import

import os
import util
import h5py
from tflearn.data_utils import *

log = util.logger.get("DS CREATOR")

RAW_DIR = './raw_data/'
WIDTH = 256
HEIGHT = 256


def create_filelist(name, images_dir, predicate=lambda x: 1):
    image_names = [images_dir + i for i in os.listdir(images_dir)]
    f = open(name, 'w')
    for i in image_names:
        f.write('{0} {1}\n'.format(i, predicate(i)))
    f.close()


def create_HDF(name, output='dataset.h5', width=WIDTH, height=HEIGHT):
    log.nfo('create HDF5 dataset {0:s} {1:d}:{2:d}'.format(output, width, height))
    build_hdf5_image_dataset(name, image_shape=(width, height),
                             mode='file', output_path=output,
                             categorical_labels=True, normalize=True)


if __name__ == '__main__':
    log.nfo('create dataset, it might take a while... ')
    create_filelist('data/bank.lst', RAW_DIR, lambda x: 1)
    create_HDF('data/bank.lst', 'data/bank.h5')
