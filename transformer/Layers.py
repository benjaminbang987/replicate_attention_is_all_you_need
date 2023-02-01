''' Define the Layers '''
import torch.nn as nn
import torch
from transformer.SubLayers import MultiHeadAttention, PositionwiseFeedForward


class EncoderLayer(nn.Module):
    """
    Compose with two layers
    TODO: Read the paper and implement the Module
    TODO: implement both __init__ function and forward function
    """
    def __init__(self, d_model, d_inner, n_head, d_k, d_v, dropout=0.1):
        super(EncoderLayer, self).__init__()

    def forward(self, enc_input, slf_attn_mask=None):
        pass


class DecoderLayer(nn.Module):
    """
    TODO: Read the paper and implement the Module
    TODO: implement both __init__ function and forward function
    """

    def __init__(self, d_model, d_inner, n_head, d_k, d_v, dropout=0.1):
        super(DecoderLayer, self).__init__()

    def forward(self, dec_input, enc_output, slf_attn_mask=None, dec_enc_attn_mask=None):
        pass