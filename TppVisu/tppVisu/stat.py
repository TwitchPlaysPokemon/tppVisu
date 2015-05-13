'''
Created on 29.04.2015

@author: Felk
'''

class Stat(object):
    '''class for pokemon stats.
    includes the base power, stages, and can calculate the final value.'''
    def __init__(self, base, stage=0):
        self.base = base
        self.stage = stage
        self.multiplier = 1
        self.increment = 1 # for abilities 'Contrary', 'Simple' and 'Unaware'
        self.multTable = [2/8, 2/7, 2/6, 2/5, 2/4, 2/3, 2/2, 3/2, 4/2, 5/2, 6/2, 7/2, 8/2]
        
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
    '''same as Stat, but overwrites the multiplication table to be applicable for Accuracy and Evasion.
    Don't use Stat for Accuracy and Evasion. Also don't use StatAccEva for atk, def, spa, spd or spe.'''
    def __init__(self, stage=0):
        super().__init__(1, stage)
        self.multTable = [33/100, 36/100, 43/100, 50/100, 60/100, 75/100, 100/100, 133/100, 166/100, 200/100, 250/100, 266/100, 300/100]
    
    def get(self):
        # overwritten, because accuracy modifiers must not be cast to an integer
        return self.base * self.multTable[self.stage + 6] * self.multiplier
