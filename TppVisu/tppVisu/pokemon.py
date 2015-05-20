'''
Created on 28.04.2015

@author: Felk
'''
from __future__ import division

from tppVisu.stat import Stat, StatAccEva
from tppVisu.tables import abilityFuncs
from tppVisu.util import Stages, TypeSet, Effs, enum


Gender = enum(male='m', female='f', none='-')

class Pokemon(object):
    '''class to represent a pokemon. Including all the needed data like types, moves, etc.'''
    def __init__(self, natID, name, type1, type2, stats, moves, gender, ability='', status='', statusVolatile='', happiness=0, level=100, weight=1, stages=Stages(0, 0, 0, 0, 0, 0, 0)):
        '''name, type1, type2, ability, status, statusVolatile are strings.
        natID is a number.
        stats is a Stats-namedtuple, see util.
        gender is an enum, see above.
        moves is an array of Move-objects, see module move.'''
        self.natID = natID
        self.name = name
        self.type1 = type1.lower() if type1 != None else None
        self.type2 = type2.lower() if type2 != None else None
        self.gender = gender
        self.ability = ability.title()  # First letters uppercase
        self.abilityVisuable = abilityFuncs.isVisuable(self.ability)
        self.moves = moves
        
        self.HP = stats.HP
        self.ATK = Stat(stats.ATK, stages.ATK)
        self.DEF = Stat(stats.DEF, stages.DEF)
        self.SPA = Stat(stats.SPA, stages.SPA)
        self.SPD = Stat(stats.SPD, stages.SPD)
        self.SPE = Stat(stats.SPE, stages.SPE)
        self.ACC = StatAccEva(stages.ACC)
        self.EVA = StatAccEva(stages.EVA)
        
        self.status = status
        self.statusVolatile = statusVolatile
        self.happiness = happiness
        self.level = level
        self.weight = weight
            
        # variables needed for calculation. Used per setup, not per pokemon
        self.stab = 1.5
        self.typeMults = TypeSet()
        self.effs = Effs(2, 1, 0.5, 0)
        self.parMult = 0.25
        self.brnMult = 0.5
        
        
    def breaksMold(self):
        return self.ability in ['Mold Breaker', 'Teravolt', 'Turboblaze']
    
    def isUntraceable(self):
        return self.ability in ['Multitype', 'Illusion', 'Flower Gift', 'Imposter', 'Stance Change', 'Trace']
    
    def disablesWeather(self):
        return self.ability in ['Cloud Nine', 'Air Lock']
    
    def hasStatusCondition(self):
        return self.status in ['brn', 'frz', 'par', 'psn', 'slp']
    
    def hasVolatileStatusCondition(self):
        return self.statusVolatile != ''  # not so clean. should check as above

