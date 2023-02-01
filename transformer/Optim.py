'''A wrapper class for scheduled optimizer '''
import numpy as np


class ScheduledOptim():
    """
    A simple wrapper class for learning rate scheduling
    TODO: Read the paper and implement the Module
    TODO: implement both __init__ function and the sub-functions
    """

    def __init__(self, optimizer, lr_mul, d_model, n_warmup_steps):


    def step_and_update_lr(self):
        """ Step with the inner optimizer """
        pass

    def zero_grad(self):
        """ Zero out the gradients with the inner optimizer """
        pass

    def _get_lr_scale(self):
        pass

    def _update_learning_rate(self):
        """Learning rate scheduling per step """
        pass

