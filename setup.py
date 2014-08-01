import os
from setuptools import setup

setup(
    name = "camcontrol",
    version = "0.1",
    author = "Royendgel Silberie",
    author_email = "royendgel@techprocur.com",
    description = ("camcontrol"),
    keywords = "mjpegtools mjpeg jpeg",
    url = "https://github.com/royendgel",
    packages=['mjpegtools'],
    classifiers=[
      'Operating System :: MacOS :: MacOS X',
      'Operating System :: Unix',
      'Development Status :: 3 - Alpha',
      'Topic :: Utilities',
      'Programming Language :: Python :: 2.7',
    ],
    include_package_data=True,
    install_requires=[],
)
