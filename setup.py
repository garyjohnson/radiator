import sys
try:
    import ez_setup
    ez_setup.use_setuptools()
except ImportError:
    pass

from setuptools import setup

setup(
    name='radiator',
    version='0.0.1',
    author='Gary Johnson',
    author_email = 'gary@gjtt.com',
    description = 'Cycle webpages for running an information radiator',
    license = 'GNU GPLv3',
    packages = ['radiator'],
    )
