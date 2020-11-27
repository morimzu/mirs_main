class Order:
    def __init__(self, target, act1, act2, time):
        self.target = target
        self.act1 = act1
        self.act2 = act2
        self.time = time

        if self.target == 'r':
            self.order = self.format_run()
        else:
            self.order = self.format_other()
    
    def format_run(self):
        order = self.target + ';' + str(self.act1) + ';' + str(self.act2) + ';' + str(self.time) + ':'
        return order
    
    def format_other(self):
        order = self.target + ';' + str(self.act1) + ';' + str(self.time) + ':'
        return order