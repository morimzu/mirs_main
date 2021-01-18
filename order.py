import numpy as np

class Order:
    def __init__(self, target, act1, act2):
        self.target = target
        self.act1 = act1
        self.act2 = act2
        self.order = self.format()
    
    def format(self):
        if np.abs(self.act2) < 10:
            if self.act2 < 0:
                order = self.target + ';' + str(self.act1) + ';' + '-0' + str(np.abs(self.act2)) + ':'
            else:
                order = self.target + ';' + str(self.act1) + ';' + '0' + str(np.abs(self.act2)) + ':'
        else:
            order = self.target + ';' + str(self.act1) + ';' + str(self.act2) + ':'
        return order