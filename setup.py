#!/usr/bin/env python
"""
wnyc_audio_workflow
======

WNYC's Audio Workflow
"""

from setuptools import setup

setup(
    name='waaa',
    version='0.0.1',
    author='Adam DePrince',
    author_email='adeprince@nypublicradio.org',
    description='Audio_Workflow',
    long_description=__doc__,
    py_modules = [
        "wnyc_waaa/__init__",
        "wnyc_waaa/uploader",
        ],
    packages = ["waaa"],
    zip_safe=True,
    license='GPL',
    include_package_data=True,
    classifiers=[
        ],
    scripts = [
        'scripts/waaa_upload_receiver'
        ],
    url = "https://github.com/wnyc/audio_workflow",
    install_requires = [
        "python-gflags",
        ]
)

