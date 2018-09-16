#!/bin/bash

upload_testing() {
    rm -rf dist

    python3 setup.py sdist bdist_wheel

    twine upload --repository-url https://test.pypi.org/legacy/ dist/*
}

rm -rf dist

python3 setup.py sdist bdist_wheel

if [ $1 = "test" ]
then
    twine upload --repository-url http://test.pypi.org/legacy/ dist/*
else
    twine upload dist/*
fi