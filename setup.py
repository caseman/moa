# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='moa -- Master of ASCII',
    version='0.1.0',
    description='A space conquest game in an ASCII universe',
    long_description=readme,
    author='Casey Duncan',
    author_email='casey.duncan@gmail.com',
    url='https://github.com/caseman/moa',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

