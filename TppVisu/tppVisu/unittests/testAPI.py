'''
Created on 28.04.2015

@author: Felk
'''

import unittest

from tppVisu.move import MoveCategory, Move
from tppVisu.pokemon import Pokemon, Gender
from tppVisu.util import Stats, Environment
from tppVisu.api import buildDictSetup
import json


class TppVisuApiTests(unittest.TestCase):
    
    def genStats(self, HP=100, ATK=100, DEF=100, SPA=100, SPD=100, SPE=100):
        return Stats(HP, ATK, DEF, SPA, SPD, SPE)
    
    def genMove(self, name='Testmove', type='normal', category=MoveCategory.physical, power=100, pp=10, accuracy=100):
        return Move(name, 'For unittests.', type, category, power, pp, accuracy)
    
    def genPkmn(self, name='Testpokemon', type1='normal', type2=None,
                   stats=None,
                   moves=None,
                   gender=Gender.male,
                   ability="Testability"):
        return Pokemon(0, name, type1, type2,
                       stats if stats != None else self.genStats(),
                       moves if moves != None else [self.genMove()],
                       gender, ability)
        
    def getDamage(self, power, ATK, DEF, mult=1):
        dmg = ((210/250) * (ATK/DEF) * power + 2) * mult
        return (dmg*0.85, dmg)
        
    def genEnv(self, weather='none'):
        return Environment(weather)
        
    def test_json1(self):
        p1 = self.genPkmn(moves=[self.genMove(category=MoveCategory.nonDamaging), self.genMove(category=MoveCategory.special)])
        dic = buildDictSetup(p1, self.genPkmn(), self.genEnv())
        self.assertEqual(json.dumps(dic, sort_keys=True), '{"blue": [{"accuracy": 100, "damage": null, "eff": "normal", "kind": "status", "speed": 100}, {"accuracy": 100, "damage": [109, 129], "eff": "normal", "kind": "normal", "speed": 100}], "red": [{"accuracy": 100, "damage": [109, 129], "eff": "normal", "kind": "normal", "speed": 100}], "weather": "none"}')
    

if __name__ == '__main__':
    unittest.main()
    
