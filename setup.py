"""
TopograPy Setup
"""

from setuptools import setup

setup(name='topograpy',
      version='0.1',
      description='Coordinate Generator for Height Maps',
      url='http://github.com/mitgobla/TopograPy',
      author='Ben Dodd',
      author_email='ben-dodd@outlook.com',
      license='MIT',
      packages=['topograpy'],
      install_requires=[
          'pillow',
      ],
      zip_safe=False)
