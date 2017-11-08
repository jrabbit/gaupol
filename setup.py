#! /usr/bin/env python

import os
import re

from setuptools import setup


def get_aeidon_version():
    """Return version number from aeidon/__init__.py."""
    path = os.path.join("aeidon", "__init__.py")
    text = open(path, "r", encoding="utf_8").read()
    return re.search(r"__version__ *= *['\"](.*?)['\"]", text).group(1)

setup(name="aeidon",
      version=get_aeidon_version(),
      packages=["aeidon",],
      author="Osmo Salomaa",
      author_email="otsaloma@iki.fi",
      url="https://otsaloma.io/gaupol/",
      license="GPLv3",
      classifiers=["License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
                   "Topic :: Multimedia :: Video",
                   "Programming Language :: Python :: 3",]
      )
