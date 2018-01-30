# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from rssbot import __version__

with open("README.rst", "r") as f:
    readme = f.read()

setup(
    name='rss-transmission',
    version=__version__,
    description='Rss plugin for transmission with a web ui',
    long_description=readme,
    keywords='rss transmission webui',
    author="helloqiu",
    author_email="helloqiu95@gmail.com",
    url='https://github.com/helloqiu/rss-transmission',
    packages=find_packages(),
    include_package_data=True,
    install_requires=open("requirements.txt").readlines(),
    license="GPLv3",
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python"
    ],
    setup_requires=[
        "pytest-runner",
    ],
    tests_require=[
        "pytest",
    ],
)
