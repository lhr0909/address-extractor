#!/usr/bin/env bash

# from https://github.com/johnlonganecker/libpostal-rest-docker/blob/master/build_libpostal.sh

mkdir -p /opt/libpostal_data

./bootstrap.sh
./configure --datadir=/opt/libpostal_data
make
make install

ldconfig
