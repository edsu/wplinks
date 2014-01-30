import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['test.py']
        self.test_suite = True
    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

setup( 
    name = 'wplinks',
    version = '0.0.4',
    url = 'http://github.com/edsu/wplinks',
    author = 'Ed Summers',
    author_email = 'ehs@pobox.com',
    license = 'http://creativecommons.org/publicdomain/zero/1.0/',
    py_modules = ['wplinks'],
    description = 'find wikipedia articles that links to a website',
    tests_require = ['pytest'],
    cmdclass = {'test': PyTest}
)
