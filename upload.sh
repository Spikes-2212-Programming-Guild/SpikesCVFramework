#!/bin/bash
rm -rf dist

python3 setup.py sdist bdist_wheel

if [ $1 = "test" ]
then
    twine upload --repository-url http://test.pypi.org/legacy/ dist/*
else
    twine upload dist/*
fi