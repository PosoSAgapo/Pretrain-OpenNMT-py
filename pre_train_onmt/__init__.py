""" Main entry point of the ONMT library """
import pre_train_onmt.inputters
import pre_train_onmt.encoders
import pre_train_onmt.decoders
import pre_train_onmt.models
import pre_train_onmt.utils
import pre_train_onmt.modules
from pre_train_onmt.trainer import Trainer
import sys
import pre_train_onmt.utils.optimizers
pre_train_onmt.utils.optimizers.Optim = pre_train_onmt.utils.optimizers.Optimizer
sys.modules["onmt.Optim"] = pre_train_onmt.utils.optimizers

# For Flake
__all__ = [pre_train_onmt.inputters, pre_train_onmt.encoders, pre_train_onmt.decoders, pre_train_onmt.models,
           pre_train_onmt.utils, pre_train_onmt.modules, "Trainer"]

__version__ = "2.2.0"
