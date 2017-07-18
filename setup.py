from distutils.core import setup
from setuptools import setup, find_packages
from codecs import open
from os import path


setup(
    name='gambling',
    version='2017.07',
    packages=['dice', 'cards', 'player'],
    url='https://github.com/SubZeb/gambling',
    license='MIT',
    author='CJ Stein',
    author_email='cjstein9@gmail.com',
    description='A package to create the necessary components for gambling including cards and dice.'
)
