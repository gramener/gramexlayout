#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from pathlib import Path


setup(
    name='gramexlayout',
    version='0.1.0',
    description='Layout algorithms for visualizations',
    long_description=(Path(__file__).parent / 'README.md').read_text(),
    long_description_content_type='text/markdown',
    author='S Anand',
    author_email='s.anand@gramener.com',
    project_urls={
        'Documentation': 'https://github.com/gramener/gramexlayout/',
        'Source': 'https://github.com/gramener/gramexlayout/',
        'Tracker': 'https://github.com/gramener/gramexlayout/issues',
    },
    url='https://github.com/gramener/gramexlayout',
    packages=['gramexlayout'],
    install_requires=['pandas'],
    license='MIT',
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    # test_suite='tests',
    # tests_require=['lxml'],
)
