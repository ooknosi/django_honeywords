"""Django Honeywords Package Setup

"""
import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-honeywords',
    version='0.1.0b2',
    packages=find_packages('src', exclude=['config',]),
    package_dir={'':'src'},
    include_package_data=True,
    license='Apache Software License',
    description=(
        'Django implementation of the Honeywords Project'
        ),
    long_description=README,
    keywords='django honeywords password login security',
    url='https://github.com/ooknosi/django_honeywords',
    download_url='https://github.com/ooknosi/django_honeywords/archive/0.1.0b2.tar.gz',
    author='Edison KOO',
    #author_email='',
    install_requires=[
        'Django',
        ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
