'''
Created on 28.04.2015

@author: Felk
'''

import unittest

from tppVisu.move import MoveCategory, Move
from tppVisu.pokemon import Pokemon, Gender
from tppVisu.tables.typeEffs import getEff
from tppVisu.util import Stats, Environment


class TppVisuMiscTests(unittest.TestCase):
    
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
        
    def test_stats1(self):
        p = self.genPkmn(stats=self.genStats(HP=100, ATK=90, DEF=80, SPA=70, SPD=60, SPE=50))
        self.assertEqual(p.HP, 100)
        self.assertEqual(p.ATK.get(), 90)
        self.assertEqual(p.DEF.get(), 80)
        self.assertEqual(p.SPA.get(), 70)
        self.assertEqual(p.SPD.get(), 60)
        self.assertEqual(p.SPE.get(), 50)
        
    def test_stats2(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100))
        p.ATK.stageAdd(1)
        p.DEF.stageAdd(2)
        p.SPA.stageAdd(3)
        p.SPD.stageAdd(4)
        p.SPE.stageAdd(5)
        self.assertEqual(p.ATK.get(), 150)
        self.assertEqual(p.DEF.get(), 200)
        self.assertEqual(p.SPA.get(), 250)
        self.assertEqual(p.SPD.get(), 300)
        self.assertEqual(p.SPE.get(), 350)
        p.ATK.stageAdd(5)
        self.assertEqual(p.ATK.get(), 400)
        
    def test_stats3(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100))
        p.ATK.stageAdd(-1)
        p.DEF.stageAdd(-2)
        p.SPA.stageAdd(-3)
        p.SPD.stageAdd(-4)
        p.SPE.stageAdd(-5)
        self.assertEqual(p.ATK.get(), int(200 / 3))
        self.assertEqual(p.DEF.get(), int(200 / 4))
        self.assertEqual(p.SPA.get(), int(200 / 5))
        self.assertEqual(p.SPD.get(), int(200 / 6))
        self.assertEqual(p.SPE.get(), int(200 / 7))
        p.ATK.stageAdd(-5)
        self.assertEqual(p.ATK.get(), int(200 / 8))
        
    def test_stats4(self):
        p = self.genPkmn()
        p.EVA.stageAdd(1)
        p.ACC.stageAdd(2)
        self.assertEqual(p.EVA.get(), 133 / 100)
        self.assertEqual(p.ACC.get(), 166 / 100)
        p.EVA.stageAdd(2)
        p.ACC.stageAdd(2)
        self.assertEqual(p.EVA.get(), 200 / 100)
        self.assertEqual(p.ACC.get(), 250 / 100)
        p.EVA.stageAdd(2)
        p.ACC.stageAdd(2)
        self.assertEqual(p.EVA.get(), 266 / 100)
        self.assertEqual(p.ACC.get(), 300 / 100)
        
    def test_stats5(self):
        p = self.genPkmn()
        p.EVA.stageAdd(-1)
        p.ACC.stageAdd(-2)
        self.assertEqual(p.EVA.get(), 75 / 100)
        self.assertEqual(p.ACC.get(), 60 / 100)
        p.EVA.stageAdd(-2)
        p.ACC.stageAdd(-2)
        self.assertEqual(p.EVA.get(), 50 / 100)
        self.assertEqual(p.ACC.get(), 43 / 100)
        p.EVA.stageAdd(-2)
        p.ACC.stageAdd(-2)
        self.assertEqual(p.EVA.get(), 36 / 100)
        self.assertEqual(p.ACC.get(), 33 / 100)
        
    def test_stats6(self):
        p = self.genPkmn(stats=self.genStats(ATK=93))
        p.ATK.stageAdd(1)
        self.assertEqual(p.ATK.get(), int(93*1.5))
        p.ATK *= 2
        self.assertEqual(p.ATK.get(), int(93*1.5*2))
        p.ATK.stageAdd(2)
        self.assertEqual(p.ATK.get(), int(93*2.5*2))
        p.ATK = p.ATK * 0.5
        self.assertEqual(p.ATK.get(), int(93*2.5))
        
    def test_moveMinMaxHits(self):
        m1 = self.genMove(name='Double Slap')
        m2 = self.genMove(name='Triple Kick')
        m3 = self.genMove(name='Tackle')
        self.assertEqual(m1.minMaxHits, (2, 5))
        self.assertEqual(m2.minMaxHits, (1, 3))
        self.assertEqual(m3.minMaxHits, (1, 1))
        
    def test_movePriority(self):
        m1 = self.genMove(name='Helping Hand')
        m2 = self.genMove(name='Extreme Speed')
        m3 = self.genMove(name='Mirror Coat')
        m4 = self.genMove(name='Flamethrower')
        self.assertEqual(m1.priority, 5)
        self.assertEqual(m2.priority, 1)
        self.assertEqual(m3.priority, -5)
        self.assertEqual(m4.priority, 0)
        
    def test_moveVisuable(self):
        m1 = self.genMove(name='Endeavor')
        m2 = self.genMove(name='Hidden Power')
        m3 = self.genMove(name='Hidden Power Psychic')
        m4 = self.genMove(name='Frustration')
        self.assertFalse(m1.visuable)
        self.assertFalse(m2.visuable)
        self.assertTrue(m3.visuable)
        self.assertTrue(m4.visuable)
        
    def test_typeEffs(self):
        self.assertEqual(getEff('water', 'fire'), 2)
        self.assertEqual(getEff('water', 'rock') * getEff('water', 'ground'), 4)
        self.assertEqual(getEff('water', 'water'), 0.5)
        self.assertEqual(getEff('grass', 'steel'), 0.5)
        self.assertEqual(getEff('ghost', 'normal'), 0)
        self.assertEqual(getEff('water', 'flying'), 1)
    
    #def test_json1(self):
    #    p1 = self.genPkmn(moves=[self.genMove(category=MoveCategory.nonDamaging), self.genMove(category=MoveCategory.special)])
    #    dic = buildDictSetup(p1, self.genPkmn(), self.genEnv())
    #    self.assertEqual(json.dumps(dic, sort_keys=True), '{"blue": [{"accuracy": 100, "damage": null, "eff": "normal", "kind": "status"}, {"accuracy": 100, "damage": [109.64999999999999, 129.0], "eff": "normal", "kind": "normal"}], "red": [{"accuracy": 100, "damage": [109.64999999999999, 129.0], "eff": "normal", "kind": "normal"}]}')
    

if __name__ == '__main__':
    unittest.main()
    
