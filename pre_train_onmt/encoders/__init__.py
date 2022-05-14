"""Module defining encoders."""
from pre_train_onmt.encoders.encoder import EncoderBase
from pre_train_onmt.encoders.transformer import TransformerEncoder
from pre_train_onmt.encoders.ggnn_encoder import GGNNEncoder
from pre_train_onmt.encoders.rnn_encoder import RNNEncoder
from pre_train_onmt.encoders.cnn_encoder import CNNEncoder
from pre_train_onmt.encoders.mean_encoder import MeanEncoder


str2enc = {"ggnn": GGNNEncoder, "rnn": RNNEncoder, "brnn": RNNEncoder,
           "cnn": CNNEncoder, "transformer": TransformerEncoder,
           "mean": MeanEncoder}

__all__ = ["EncoderBase", "TransformerEncoder", "RNNEncoder", "CNNEncoder",
           "MeanEncoder", "str2enc"]
