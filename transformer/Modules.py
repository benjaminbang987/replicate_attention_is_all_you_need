import torch
import torch.nn as nn
import torch.nn.functional as F


class ScaledDotProductAttention(nn.Module):
    """
    Scaled Dot-Product Attention
    TODO: Read the paper and implement the Module
    TODO: implement both __init__ function and forward function
    """

    def __init__(self, temperature, attn_dropout=0.1):
        super().__init__()

    def forward(self, q, k, v, mask=None):
        pass
