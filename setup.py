# coding=utf-8
import sys

cmdclass = {}

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
else:
    from setuptools.command.test import test as TestCommand

    class PyTest(TestCommand):
        def initialize_options(self):
            TestCommand.initialize_options(self)
            self.pytest_args = []

        def finalize_options(self):
            TestCommand.finalize_options(self)
            self.test_args = []
            self.test_suite = True

        def run_tests(self):
            # import here, cause outside the eggs aren't loaded
            import pytest
            errno = pytest.main(self.pytest_args)
            sys.exit(errno)

    cmdclass['test'] = PyTest


setup(
    name='openprovider.py',
    version='0.10.4',
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
        "betamax>=0.7.0",
        "fake-factory",
        "pytest",
    ],
    cmdclass=cmdclass,
)
