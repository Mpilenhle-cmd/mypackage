from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='1.0',
    packages=find_packages(exclude=['tests*']), 
    license = 'MIT',
    description = 'EDSA example python package', 
    long_description=open('README.md').read(),
    install_requires = ['numpy'],
    url='https://github.com/mpilenhle.cmd/MYPACKAGE',
    author='Mpilenhle Hlatshwayo',
    author_email= 'mpilenhlefezuvuyohlatshwayo@gmail.com'
)