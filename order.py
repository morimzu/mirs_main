class Order:
    def __init__(self, target, act1, act2):
        self.target = target
        self.act1 = act1
        self.act2 = act2
        self.order = self.format()
    
    def format(self):
        order = self.target + ';' + str(self.act1) + ';' + str(self.act2) + ':'
        return order