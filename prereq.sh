#!/usr/bin/env bash

NAME=$(uname -s)
echo set prerequisites for ${NAME} platform ...

sudo easy_install --upgrade pip
sudo easy_install --upgrade six
sudo easy_install --upgrade ipython
sudo easy_install --upgrade numpy

if [ $NAME == "Darwin" ]; then
    if [ ! -f /usr/local/bin/brew ]; then
        echo install brew ...
        /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    fi
    brew install python
    brew install homebrew/python/scipy
    brew install coreutils
    sudo -H pip install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-0.11.0rc1-py2-none-any.whl

#   sudo -H pip install -U https://storage.googleapis.com/tensorflow/mac/gpu/tensorflow-0.11.0rc1-py2-none-any.whl
fi

if [ $NAME == "Linux" ]; then
    sudo apt-get install python-pip python-dev python-numpy python-scipy
    sudo pip install -U https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.11.0rc1-cp34-cp34m-linux_x86_64.whl
fi

sudo -H pip install -U git+https://github.com/tflearn/tflearn.git
sudo -H pip install -U h5py
