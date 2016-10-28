#!/usr/bin/env bash

NAME=$(uname -s)
echo set prerequisites for ${NAME} platform ...

if [ $NAME == "Darwin" ]; then
    if [ ! -f /usr/local/bin/brew ]; then
        echo install brew ...
        /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    fi
    brew install python
    brew install coreutils

    sudo easy_install pip
    sudo easy_install --upgrade six
    sudo pip install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-0.11.0rc1-py2-none-any.whl

#   brew tap caskroom/cask
#   brew cask install cuda

  # sudo pip install --upgrade https://storage.googleapis.com/tensorflow/mac/gpu/tensorflow-0.11.0rc1-py2-none-any.whl



fi

if [ $NAME == "Linux" ]; then
    sudo apt-get install python-pip python-dev
    sudo pip install --upgrade https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.11.0rc1-cp34-cp34m-linux_x86_64.whl
fi
