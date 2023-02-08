''' Define the Transformer model '''
import torch
import torch.nn as nn
import numpy as np
from transformer.Layers import EncoderLayer, DecoderLayer


def get_pad_mask(seq, pad_idx):
    return (seq != pad_idx).unsqueeze(-2)


def get_subsequent_mask(seq):
    """
    For masking out the subsequent info.
    TODO: Read the paper and implement the Module
    TODO: implement both __init__ function and forward function
    """


class PositionalEncoding(nn.Module):
    """
    TODO: Read the paper and implement the Module
    TODO: implement both __init__ function and forward function
    """
    def __init__(self, d_hid, n_position=200):
        super(PositionalEncoding, self).__init__()

    def _get_sinusoid_encoding_table(self, n_position, d_hid):
        """
        Sinusoid position encoding table
        TODO: Read the paper and implement the Module
        TODO: implement both __init__ function and forward function
        """

        def get_position_angle_vec(position):
            pass

        pass

    def forward(self, x):
        pass


class Encoder(nn.Module):
    """
    A encoder model with self attention mechanism.
    TODO: Read the paper and implement the Module
    TODO: implement both __init__ function and forward function
    """

    def __init__(
        self, n_src_vocab, d_word_vec, n_layers, n_head, d_k, d_v,
        d_model, d_inner, pad_idx, dropout=0.1, n_position=200, scale_emb=False
    ):
        super().__init__()

    def forward(self, src_seq, src_mask, return_attns=False):
        pass


class Decoder(nn.Module):
    """
    A decoder model with self attention mechanism.
    TODO: Read the paper and implement the Module
    TODO: implement both __init__ function and forward function
    """

    def __init__(
        self, n_trg_vocab, d_word_vec, n_layers, n_head, d_k, d_v,
        d_model, d_inner, pad_idx, n_position=200, dropout=0.1, scale_emb=False
    ):

        super().__init__()

    def forward(self, trg_seq, trg_mask, enc_output, src_mask, return_attns=False):
        pass


class Transformer(nn.Module):
    """
    A sequence to sequence model with attention mechanism.
    TODO: Read the paper and implement the Module
    TODO: implement both __init__ function and forward function
    """

    def __init__(
        self, n_src_vocab, n_trg_vocab, src_pad_idx, trg_pad_idx,
        d_word_vec=512, d_model=512, d_inner=2048,
        n_layers=6, n_head=8, d_k=64, d_v=64, dropout=0.1, n_position=200,
        trg_emb_prj_weight_sharing=True, emb_src_trg_weight_sharing=True,
        scale_emb_or_prj='prj'
    ):

        super().__init__()


    def forward(self, src_seq, trg_seq):
        pass

