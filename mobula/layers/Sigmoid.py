from .Layer import *

class Sigmoid(Layer):
    def __init__(self, model, *args, **kwargs):
        Layer.__init__(self, model, *args, **kwargs)
    def __str__(self):
        return "It is a Sigmoid Layer"
    def reshape(self):
        self.Y = np.zeros(self.X.shape)
    def reshape2(self):
        self.dX = np.zeros(self.X.shape)
    def forward(self):
        self.Y = np.clip(1.0 / (1.0 + np.exp(-self.X)), 1e-16, 1.0 - 1e-16)
    def backward(self):
        self.dX = np.multiply(self.dY, np.multiply(self.Y, 1.0 - self.Y))
