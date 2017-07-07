#!/usr/bin/env python

from setuptools import setup

__version__ = '0.1.0'

setup(name='GuessThatSong',
      version=__version__,
      install_requires=['Flask==0.12.1',
					'SQLAlchemy>=1.1.9',
                    'Flask-SQLAlchemy>=2.2',
                    'Flask-WTF==0.14',
                    'gunicorn==19.7.1',
                    ],
      description='Song Trivia Game Web Application',
      long_description=open('README.md').read(),
      author='Matt Murch',
      author_email='mattmurch@gmail.com',
      url='https://github.com/mattmurch/GuessThatSong',
      download_url='https://github.com/mattmurch/GuessThatSong/tarball/' + __version__,
      scripts=['run.py'],
      license='MIT',
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Framework :: Flask',
          'Intended Audience :: End Users/Desktop',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Topic :: Games/Entertainment',
      ],
      keywords=('music trivia guessing game'),
      packages=['app',
      ],
)
