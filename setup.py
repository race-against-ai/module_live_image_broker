# Copyright (C) 2023, NG:ITL
import versioneer
from pathlib import Path
from setuptools import find_packages, setup


def read(fname):
    return open(Path(__file__).parent / fname).read()


setup(
    name="raai_module_live_image_broker",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="Torsten Wylegala",
    author_email="mail@twyleg.de",
    description=("Image broker to receive live image from one source and pass it onto another."),
    license="GPL 3.0",
    keywords="image broker",
    url="https://github.com/vw-wob-it-edu-ngitl/raai_module_live_image_broker",
    packages=find_packages(),
    long_description=read("README.md"),
    install_requires=["pynng~=0.7.2"],
)
