"""Module defining inputters.

Inputters implement the logic of transforming raw data to vectorized inputs,
e.g., from a line of text to a sequence of embeddings.
"""
from pre_train_onmt.inputters.inputter import get_fields, build_vocab, filter_example
from pre_train_onmt.inputters.iterator import max_tok_len, OrderedIterator
from pre_train_onmt.inputters.dataset_base import Dataset, DynamicDataset
from pre_train_onmt.inputters.text_dataset import text_sort_key, TextDataReader
from pre_train_onmt.inputters.datareader_base import DataReaderBase

str2reader = {
    "text": TextDataReader}
str2sortkey = {
    'text': text_sort_key}


__all__ = ['Dataset', 'get_fields', 'DataReaderBase', 'filter_example',
           'build_vocab', 'OrderedIterator', 'max_tok_len',
           'text_sort_key', 'TextDataReader', 'DynamicDataset']
