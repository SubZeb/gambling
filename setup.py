from distutils.core import setup
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='gambling',
    version='1.0.0.dev2',
    url='https://github.com/SubZeb/gambling',
    license='MIT',
    author='CJ Stein',
    author_email='cjstein9@gmail.com',
    description='A package to create the necessary components for gambling including cards and dice.',
    keywords='cards card dice gambling poker blackjack',
    packages=find_packages(),
    python_requires='>=3'
)
