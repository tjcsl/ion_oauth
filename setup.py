#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


setup(name="ion_oauth",
      description="python-social-auth plugin for ion",
      long_description=long_description,
      long_description_content_type="text/markdown",
      version="0.2",
      license="GPL",
      author="The TJHSST Computer Systems Lab",
      author_email="intranet@tjhsst.edu",
      url="https://github.com/tjcsl/ion_oauth",
      zip_safe=True,
      install_requires=['python-social-auth'],
      packages=find_packages(),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
      ])
