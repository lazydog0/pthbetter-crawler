#!/usr/bin/env python
'''
Installer script for redbetter.
'''

from setuptools import setup

import re
VERSIONFILE="_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

setup(
    name = "redbetter",
    description = "Automatically transcode and upload FLACs on Redacted.",
    author = 'lazydog',
    author_email = '',
    version = verstr,
    url = 'http://github.com/lazydog0/redbetter-crawler',
    py_modules = [
        '_version',
        'tagging',
        'transcode',
        'redapi',
        'whatapi'
    ],
    scripts = ['redbetter'],
    install_requires = [
        'mutagen',
        'mechanize',
        'requests'
    ]
)
