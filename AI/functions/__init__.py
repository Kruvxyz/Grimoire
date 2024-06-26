import torch

__all__ = ['get_device']

def get_device():
    try:
        return torch.device('cuda' if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else 'cpu')
    except:
        return torch.device('cpu')