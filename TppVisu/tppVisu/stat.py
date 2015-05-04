'''
Created on 29.04.2015

@author: Felk
'''

class Stat(object):
    '''
    class for pokemon stats.
    includes the base power, stages, and can calculate the final value.
    '''
    def __init__(self, base, stage=0):
        self.base = base
        self.stage = stage
        self.multiplier = 1
        self.increment = 1 # for abilities 'Contrary', 'Simple' and 'Unaware'
        self.multTable = [1/4, 2/7, 1/3, 2/5, 1/2, 2/3, 1, 3/2, 2, 5/2, 3, 7/2, 4]
        
    def setStage(self, stage):
        self.stage = min(6, max(-6, stage))
        
    def stageAdd(self, step=1):
        self.setStage(self.stage + step * self.increment)
        
    def get(self):
        # +6 because stages are within -6 and 6, but indices are 0 to 12
        return int(self.base * self.multTable[self.stage + 6] * self.multiplier)
        
    def __mul__(self, other):
        self.multiplier *= other
        return self
        
class StatAccEva(Stat):
    def __init__(self, stage=0):
        super().__init__(1, stage)
        self.multTable = [1/3, 3/8, 3/7, 1/2, 3/5, 3/4, 1, 4/3, 5/3, 2, 7/3, 8/3, 3]
        
