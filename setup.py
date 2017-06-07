import os
from setuptools import setup, find_packages
from pip.req import parse_requirements
from pip.download import PipSession

import pip
pip.main(['install','-r','requirements.txt'])

setup(
    name='etf_holdings',
    version='0.0.1',
    packages=find_packages(),
    author = "Tommy Carpenter",
    author_email = "tommyjcarpenter@gmail.com",
    description='Given several ETFs, finds the weighted percentage/allocation of underlying holdings'
    license = "MIT",
    keywords = "",
    url = "",
    zip_safe=False,
)
