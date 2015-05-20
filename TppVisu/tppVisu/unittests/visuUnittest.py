'''
Created on 13.05.2015

@author: Felk
'''
from __future__ import division

import unittest
from tppVisu.pokemon import Pokemon, Gender
from tppVisu.move import Move, MoveCategory
from tppVisu.util import Stats, Environment, Eff

class VisuTestCase(unittest.TestCase):
    
    def genStats(self, HP=100, ATK=100, DEF=100, SPA=100, SPD=100, SPE=100):
        return Stats(HP, ATK, DEF, SPA, SPD, SPE)
    
    def genMove(self, name='Testmove', type='normal', category=MoveCategory.physical, power=100, pp=10, accuracy=100):
        return Move(name, 'For unittests.', type, category, power, pp, accuracy)
    
    def genPkmn(self, name='Testpokemon', type1='normal', type2=None,
                   stats=None,
                   moves=None,
                   gender=Gender.male,
                   ability="Testability",
                   id=0):
        return Pokemon(id, name, type1, type2,
                       stats if stats != None else self.genStats(),
                       moves if moves != None else [self.genMove()],
                       gender, ability)
        
    def getDamage(self, power, ATK, DEF, mult=1):
        dmg = ((210/250) * (ATK/DEF) * power + 2) * mult
        return (int(dmg*0.85), int(dmg))
     
    def genEnv(self, weather='none'):
        return Environment(weather)
        
    def assertNotEffective(self, result):
        self.assertEqual(result.eff, Eff.NOT)
        
    def assertWeakEffective(self, result):
        self.assertEqual(result.eff, Eff.WEAK)
        
    def assertNormalEffective(self, result):
        self.assertEqual(result.eff, Eff.NORMAL)
        
    def assertSuperEffective(self, result):
        self.assertEqual(result.eff, Eff.SUPER)
