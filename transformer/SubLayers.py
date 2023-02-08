import torch.nn as nn
import torch.nn.functional as F
from transformer.Modules import ScaledDotProductAttention


class MultiHeadAttention(nn.Module):
    """
    Multi-Head Attention module
    TODO: Read the paper and implement the Module
    TODO: implement both __init__ function and forward function
    """
    def __init__(self, n_head, d_model, d_k, d_v, dropout=0.1):
        super().__init__()

    def forward(self, q, k, v, mask=None):
        pass


class PositionwiseFeedForward(nn.Module):
    """
    TODO: Read the paper and implement the Module
    TODO: implement both __init__ function and forward function
    """
    def __init__(self, d_in, d_hid, dropout=0.1):
        super().__init__()

    def forward(self, x):
        pass
