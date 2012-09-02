#!/usr/bin/env python

from distutils.core import setup

version = '0.1'

classifiers = [
    "Development Status :: 2 - Beta",
    "Framework :: Django",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU General Public License (GPL)",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Topic :: Internet :: WWW/HTTP",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

setup(
    name='django-metatags',
    version=version,
    url='http://github.com/cpharmston/django-metatags',
    author='Chuck Harmston',
    author_email='chuck@chuckharmston.com',
    license='Dual-licensed under MIT and GPL',
    packages=['metatags', 'generic_links.templatetags'],
    package_dir={'metatags': 'metatags'},
    description=(
        'A simple, pluggable app for attaching meta tags to objects with their '
        'own views.'
    ),
    classifiers=classifiers,
)
