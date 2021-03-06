#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

long_description = 'Autosub is a utility for automatic speech recognition and subtitle generation. It takes a video or an audio file as input, performs voice activity detection to find speech regions, makes parallel requests to Google Web Speech API to generate transcriptions for those regions, (optionally) translates them to a different language, and finally saves the resulting subtitles to disk. It supports a variety of input and output languages (to see which, run the utility with --list-src-languages and --list-dst-languages as arguments respectively) and can currently produce subtitles in either the SRT format or simple JSON.'

setup(
    name='autosub',
    version='0.3.12',
    description='Auto-generates subtitles for any video or audio file',
    long_description=long_description,
    author='Anastasis Germanidis',
    author_email='agermanidis@gmail.com',
    url='https://github.com/agermanidis/autosub',
    packages=['autosub'],
    scripts=['bin/autosub', 'bin/autosub_regions', 'bin/autosub_energies', 'bin/autosub_regions_from_srt'],
    install_requires=[
        'google-api-python-client>=1.4.2',
        'requests>=2.3.0',
        'pysrt>=1.0.1',
        'progressbar>=2.3;python_version<"3.0"',
        'progressbar33>=2.4;python_version>="3.0"'
    ],
    license=open("LICENSE").read()
)
