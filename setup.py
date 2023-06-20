# Copyright (C) 2023, NG:ITL
from pathlib import Path
from setuptools import find_packages, setup

NAME = 'live_image_broker'
VERSION = '0.0.1'


def read(fname):
    return open(Path(__file__).parent / fname).read()


setup(
    name=NAME,
    version=VERSION,
    author="Torsten Wylegala",
    author_email="mail@twyleg.de",
    description=("Image broker to receive live image from one source and pass it onto another."),
    license="GPL 3.0",
    keywords="image broker",
    url="https://github.com/vw-wob-it-edu-ngitl/race_against_ai",
    packages=find_packages(),
    long_description=read('README.md'),
    install_requires=[
        "pynng~=0.7.2"
    ],
    cmdclass={}
)
