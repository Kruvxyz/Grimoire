import AI as AI

__all__ = [
    "AI",
    "get_device",
    "GRU",
    "LSTM",
    "RNN",
    "__version__",
]

class Grimoire:
    def __init__(self):
        self.AI = AI
        self.get_device = AI.functions.get_device
        __version__ = "0.0.1"

_inst = Grimoire()
__version__ = _inst.__version__
get_device = _inst.get_device
GRU = _inst.AI.RNN.GRU
LSTM = _inst.AI.RNN.LSTM
RNN = _inst.AI.RNN.RNN