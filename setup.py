#!/usr/bin/env python

from setuptools import setup

slacker_version = 'slacker>=0.9.0'
install_requires = [ slacker_version ]

setup(
        name = 'cheryl',
        version = '0.1.0',
        description = 'Easy slack posting direct message bot tool',
        author = 'Daiki Shimada',
        author_email = 'daiki.shimada.9g@stu.hosei.ac.jp',
        url = '',
        install_requires = install_requires,
        license='http://www.apache.org/licenses/LICENSE-2.0'
    )
