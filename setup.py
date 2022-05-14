#!/usr/bin/env python
from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Pre-train-OpenNMT-py',
    description='A python onmt extension that supports pre-train model implementation of OpenNMT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='o_2.2.0_p_0.0.1',
    packages=find_packages(),
    python_requires=">=3.5",
    install_requires=[
        "torch>=1.6.0",
        "torchtext==0.5.0",
        "configargparse",
        "tensorboard>=2.3",
        "flask",
        "waitress",
        "pyonmttok>=1.23,<2",
        "pyyaml",
        "transformers"
    ],
    entry_points={
        "console_scripts": [
            "pre_train_onmt_server=pre_train_onmt.bin.server:main",
            "pre_train_onmt_train=pre_train_onmt.bin.train:main",
            "pre_train_onmt_translate=pre_train_onmt.bin.translate:main",
            "pre_train_onmt_translate_dynamic=pre_train_onmt.bin.translate_dynamic:main",
            "pre_train_onmt_release_model=pre_train_onmt.bin.release_model:main",
            "pre_train_onmt_average_models=pre_train_onmt.bin.average_models:main",
            "pre_train_onmt_build_vocab=pre_train_onmt.bin.build_vocab:main"
        ],
    }
)
