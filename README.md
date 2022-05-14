# Pretrain-OpenNMT-py: Open-Source Neural Machine Translation in Pretrain Version

This repository is an extension from OpenNMT-py which supports the pre-train model including BERT model or other pre-trained models. The target of this branch is to make OpenNMT a research friendly project that support pre-train model, auto evaluation and find the best checkpoint on the test set.
Before you use this package, you should refer to [OpenNMT](https://github.com/OpenNMT/OpenNMT-py) for basic usage as this package works as extension. 

However, as this is an independent extension for OpenNMT, so I may not be able to always keep maintain updated with OpenNMT's new release, but I will try my best. If any  feature of OpenNMT does not work in here, you should use OpenNMT instead, but if you think it is a bug in the repository, please raise an issue.
## Completed Features:
### BERT as Embedding
In this feature, BERT works as an embedding layer that provide work embedding given a token. Therefore the BERT is not the encoder at this feature, the RNN or any other model can be chosen to be the encoder.
### BERT as Encoder
In this feature, BERT works an the encoder which makes it a BERT2Seq model.
## 

## Installation
This package is not available in pip as most of the code is still experimentaly so you should install in from source.
```
git clone https://github.com/OpenNMT/OpenNMT-py.git
cd OpenNMT-py
pip install -e .
```
Note: if you encounter a MemoryError during installation, try to use pip with --no-cache-dir. For other installation details, please refer to OpenNMT.

## To do features:
### Generation Pre-trained Model 
This include pre-trained models like T5 or other possible generation pre-trained models.
### Parrallel Training and Inference
This feature is mainly to be research friendlym, the target is to split the test and training and then automatically find the best checkpoint.
## Others
This project will be organized and re-publish as another package since OpenNMT does not consider to include pre-trained models.

Feel free to send a PR or feature request, I will reply at my best.
