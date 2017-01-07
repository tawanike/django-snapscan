# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='django-snapscan',
    version='0.0.1',
    description='',
    long_description=long_description,
    url='https://github.com/tawanike/django-snapscan',
    author='Tawanda Abraham Makunike',
    author_email='makunike@buisoft.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Online Payments Processing :: SnapScan',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='payments,spanscan',
    packages=find_packages(exclude=['contrib', 'docs', 'tests'])
)
