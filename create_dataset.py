#!/usr/bin/env python

import os
import util

log = util.logger.get("DS")

RAW_DIR = './raw_data/'
WIDTH = 600 / 2
HEIGHT = 382 / 2


def positive(fname):
    return 1


def negative(fname):
    return 0


def create_filelist(images_dir, predicate=positive):
    image_names = [images_dir + i for i in os.listdir(images_dir)]
    f = open('train.txt', 'w')
    for i in image_names:
        f.write('{0} {1}\n'.format(i, predicate(i)))
    f.close()


log.nfo("create dataset ...")
create_filelist(RAW_DIR)















# if __name__ == '__main__':
#     pass
