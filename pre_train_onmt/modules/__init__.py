"""  Attention and normalization modules  """
from pre_train_onmt.modules.util_class import Elementwise
from pre_train_onmt.modules.gate import context_gate_factory, ContextGate
from pre_train_onmt.modules.global_attention import GlobalAttention
from pre_train_onmt.modules.conv_multi_step_attention import ConvMultiStepAttention
from pre_train_onmt.modules.copy_generator import CopyGenerator, CopyGeneratorLoss, \
    CopyGeneratorLossCompute, CopyGeneratorLMLossCompute
from pre_train_onmt.modules.multi_headed_attn import MultiHeadedAttention
from pre_train_onmt.modules.embeddings import Embeddings, PositionalEncoding
from pre_train_onmt.modules.weight_norm import WeightNormConv2d
from pre_train_onmt.modules.average_attn import AverageAttention

__all__ = ["Elementwise", "context_gate_factory", "ContextGate",
           "GlobalAttention", "ConvMultiStepAttention", "CopyGenerator",
           "CopyGeneratorLoss", "CopyGeneratorLossCompute",
           "MultiHeadedAttention", "Embeddings", "PositionalEncoding",
           "WeightNormConv2d", "AverageAttention",
           "CopyGeneratorLMLossCompute"]
