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


def _build_hdf5(target_path, image_shape, output_path='dataset.h5',
               mode='file', categorical_labels=True,
               normalize=True, grayscale=False,
               files_extension=None, chunks=True):
    assert image_shape, "Image shape must be defined."
    assert image_shape[0] and image_shape[1], \
        "Image shape error. It must be a tuple of int: ('width', 'height')."
    assert mode in ['folder', 'file'], "`mode` arg must be 'folder' or 'file'"

    if mode == 'folder':
        images, labels = directory_to_samples(target_path,
                                              flags=files_extension)
    else:
        with open(target_path, 'r') as f:
            images, labels = [], []
            for l in f.readlines():
                l = l.strip('\n').split()
                images.append(l[0])
                labels.append(int(l[1]))

    n_classes = np.max(labels) + 1

    d_imgshape = (len(images), image_shape[0], image_shape[1], 3) \
        if not grayscale else (len(images), image_shape[0], image_shape[1])
    d_labelshape = (len(images), n_classes) \
        if categorical_labels else (len(images),)

    dataset = h5py.File(output_path, 'w')
    dataset.create_dataset('X', d_imgshape, chunks=chunks)
    dataset.create_dataset('Y', d_labelshape, chunks=chunks)

    num_images = len(images)

    for i in range(num_images):

        log.dbg("{0:s}\t{1:03d}/{2:d}".format(images[i], i, num_images))

        img = load_image(images[i])
        width, height = img.size
        if width != image_shape[0] or height != image_shape[1]:
            img = resize_image(img, image_shape[0], image_shape[1])
        if grayscale:
            img = convert_color(img, 'L')
        elif img.mode == 'L':
            img = convert_color(img, 'RGB')

        img = pil_to_nparray(img)
        if normalize:
            img /= 255.
        dataset['X'][i] = img
        if categorical_labels:
            dataset['Y'][i] = to_categorical([labels[i]], n_classes)[0]
        else:
            dataset['Y'][i] = labels[i]




def create_filelist(name, images_dir, predicate=lambda x: 1):
    image_names = [images_dir + i for i in os.listdir(images_dir)]
    f = open(name, 'w')
    for i in image_names:
        f.write('{0} {1}\n'.format(i, predicate(i)))
    f.close()


def create_HDF(name, output='dataset.h5', width=WIDTH, height=HEIGHT):
    log.nfo('create HDF5 dataset {0:s} {1:d}:{2:d}'.format(output, width, height))
    _build_hdf5(name, image_shape=(width, height),
                    mode='file', output_path=output,
                    categorical_labels=True, normalize=True)


if __name__ == '__main__':
    log.nfo('create dataset, it might take a while... ')
    create_filelist('data/bank.lst', RAW_DIR, lambda x: 1)
    create_HDF('data/bank.lst', 'data/bank.h5')
