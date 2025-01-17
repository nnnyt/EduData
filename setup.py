# coding: utf-8
# create by tongshiwei on 2019/6/25

from setuptools import setup

test_deps = [
    'pytest>=4',
    'pytest-cov>=2.6.0',
    'pytest-pep8>=1',
]

setup(
    name='EduData',
    version='0.0.1',
    extras_require={
        'test': test_deps,
    },
    install_requires=[
        'mxnet',
        'tqdm',
        'networkx',
        'longling>=1.1.0',
        'requests',
        'bs4',
        'rarfile',
    ]  # And any other dependencies foo needs
)
