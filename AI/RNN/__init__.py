import torch
import torch.nn as nn


__all__ = ['GRU', 'LSTM', 'RNN']

class GRU(torch.nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, num_outputs, device=torch.device('cpu')):
        super(GRU, self).__init__()
        self.device = device
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.num_outputs = num_outputs

        self.gru = nn.GRU(input_size, hidden_size, num_layers, batch_first=True).to(self.device)
        self.linear = nn.Linear(hidden_size, num_outputs).to(self.device)


    def forward(self, x, device=None):  
        """
        Input shape: (batch_size, seq_len, input_size)
        Output shape: (batch_size, seq_len, num_outputs)
        """
        if device is None:
            device = self.device

        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(device)
        output, _ = self.gru(x.to(device), h0)
        output = self.linear(output)
        return output
    

class LSTM(torch.nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, num_outputs, device=torch.device('cpu')):
        super(LSTM, self).__init__()
        self.device = device
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.num_outputs = num_outputs

        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True).to(self.device)
        self.linear = nn.Linear(hidden_size, num_outputs).to(self.device)


    def forward(self, x, device=None):  
        """
        Input shape: (batch_size, seq_len, input_size)
        Output shape: (batch_size, seq_len, num_outputs)
        """
        if device is None:
            device = self.device

        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(device)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(device)
        output, _ = self.lstm(x.to(device), (h0, c0))
        output = self.linear(output)
        return output
    
    
class RNN(torch.nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, num_outputs, device=torch.device('cpu')):
        super(RNN, self).__init__()
        self.device = device
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.num_outputs = num_outputs

        self.rnn = nn.RNN(input_size, hidden_size, num_layers, batch_first=True).to(self.device)
        self.linear = nn.Linear(hidden_size, num_outputs).to(self.device)


    def forward(self, x, device=None):  
        """
        Input shape: (batch_size, seq_len, input_size)
        Output shape: (batch_size, seq_len, num_outputs)
        """
        if device is None:
            device = self.device

        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(device)
        output, _ = self.rnn(x.to(device), h0)
        output = self.linear(output)
        return output