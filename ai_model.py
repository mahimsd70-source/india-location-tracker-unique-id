import torch
import torch.nn as nn

class TrajectoryTransformer(nn.Module):
    def __init__(self, d_model=64):
        super().__init__()
        self.input_proj = nn.Linear(5, d_model) # lat,lng,speed,hour,day
        encoder_layer = nn.TransformerEncoderLayer(d_model=d_model, nhead=4, batch_first=True)
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=2)
        self.output = nn.Linear(d_model, 2) # next lat, lng
        
    def forward(self, x):
        # x: [batch, 30, 5]
        x = self.input_proj(x)
        x = self.transformer(x)
        return self.output(x[:, -1])

# To train later:
# model = TrajectoryTransformer()
# Train on user's past routes - it will learn his daily pattern