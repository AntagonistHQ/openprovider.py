# coding=utf-8

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import sys
unittest_requirements = ['unittest2'] if sys.version_info[:2] == (2, 6) else []

setup(
    name='openprovider.py',
    version='0.9.0',
    author='Antagonist B.V.',
    author_email='info@antagonist.nl',
    packages=['openprovider', 'openprovider.modules', 'openprovider.data'],
    url='https://github.com/AntagonistHQ/openprovider.py',
    license='LICENSE.rst',
    description='An unofficial library for the OpenProvider API',
    long_description=open('README.rst').read(),
    install_requires=[
        "requests >= 2.3.0, <= 2.5.1",
        "lxml >= 3.3.5",
    ],
    tests_require=[
        "betamax",
    ] + unittest_requirements,
    setup_requires=[
        'nose>=1.0',
        'coverage>=3.7'
    ]
)
