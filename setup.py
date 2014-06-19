# coding=utf-8

import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class Tox(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox
        errno = tox.cmdline(self.test_args)
        sys.exit(errno)


setup(
    name='openprovider.py',
    version='0.0.1',
    author='Antagonist B.V.',
    author_email='info@antagonist.nl',
    packages=find_packages(),
    url='http://pypi.python.org/pypi/openprovider.py',
    license='MIT',
    description='An unofficial library for the OpenProvider API',
    long_description=open('README.rst').read(),
    install_requires=[
        "requests >= 2.3.0",
        "lxml >= 3.3.5",
    ],
    tests_require=['tox'],
    cmdclass={'test': Tox},
)
