#!/bin/bash -e
echo "${1:?}" > boringmd/VERSION
rm -rf build
rm -rf dist
python setup.py bdist_wheel
rm -rf build
