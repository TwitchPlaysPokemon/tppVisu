'''
Created on 28.04.2015

@author: Felk
'''

import unittest

from tppVisu.move import MoveCategory, Move
from tppVisu.pokemon import Pokemon, Gender
from tppVisu.tables.typeEffs import getEff
from tppVisu.util import Stats, Environment
from tppVisu.calculator import Eff, calcMove, Kind
from tppVisu.api import buildDictSetup
import json

class TppVisuTests(unittest.TestCase):
    
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
        
    def assertNotEffective(self, result):
        self.assertEqual(result.eff, Eff.NOT)
        
    def assertWeakEffective(self, result):
        self.assertEqual(result.eff, Eff.WEAK)
        
    def assertNormalEffective(self, result):
        self.assertEqual(result.eff, Eff.NORMAL)
        
    def assertSuperEffective(self, result):
        self.assertEqual(result.eff, Eff.SUPER)
    
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
        
    def test_move_arm_thrust(self):
        m = self.genMove(name='Arm Thrust', power=15)
        p1 = self.genPkmn(stats=self.genStats(ATK=332), type1="dragon") # no stab
        p2 = self.genPkmn(stats=self.genStats(DEF=223))
        dmg1 = self.getDamage(15, 332, 223)[0] * 2
        dmg2 = self.getDamage(15, 332, 223)[1] * 5
        self.assertEqual(calcMove(m, p1, p2, self.genEnv()).damage, (dmg1, dmg2))
        
        
    def test_move_attract(self):
        m = self.genMove(name='Attract')
        p1 = self.genPkmn(gender=Gender.male)
        p2 = self.genPkmn(gender=Gender.male)
        self.assertNotEffective(calcMove(m, p1, p2, self.genEnv()))
        p2.gender = Gender.female
        self.assertNormalEffective(calcMove(m, p1, p2, self.genEnv()))
        p1.gender = Gender.none
        self.assertNotEffective(calcMove(m, p1, p2, self.genEnv()))
        
    def test_move_blizzard(self):
        m = self.genMove(name='Blizzard', accuracy=70)
        self.assertEqual(calcMove(m, self.genPkmn(), self.genPkmn(), self.genEnv()).accuracy, 70)
        self.assertEqual(calcMove(m, self.genPkmn(), self.genPkmn(), self.genEnv(weather='hail')).accuracy, 100)
        
    def test_move_dragon_rage(self):
        m = self.genMove(name='Dragon Rage')
        self.assertEqual(calcMove(m, self.genPkmn(), self.genPkmn(), self.genEnv()).damage, (40, 40))

    def test_move_explosion(self):
        m = self.genMove(name='Explosion', power=250, type='normal')
        p1 = self.genPkmn(stats=self.genStats(ATK=123), type1='normal') # stab
        p2 = self.genPkmn(stats=self.genStats(DEF=321), type1='normal')
        self.assertEqual(calcMove(m, p1, p2, self.genEnv()).damage, self.getDamage(500, 123, 321, 1.5))

    def test_move_facade(self):
        m = self.genMove(name='Facade', power=70, type='normal')
        p1 = self.genPkmn(stats=self.genStats(ATK=121), type1='fire') # no stab
        p2 = self.genPkmn(stats=self.genStats(DEF=212), type1='normal')
        self.assertEqual(calcMove(m, p1, p2, self.genEnv()).damage, self.getDamage(70, 121, 212))
        p1.status = 'par'
        self.assertEqual(calcMove(m, p1, p2, self.genEnv()).damage, self.getDamage(140, 121, 212))

    def test_move_ohko(self):
        self.assertEqual(calcMove(self.genMove(name='Fissure'), self.genPkmn(), self.genPkmn(), self.genEnv()).kind, Kind.ohko)
        self.assertEqual(calcMove(self.genMove(name='Guillotine'), self.genPkmn(), self.genPkmn(), self.genEnv()).kind, Kind.ohko)
        self.assertEqual(calcMove(self.genMove(name='Sheer Cold'), self.genPkmn(), self.genPkmn(), self.genEnv()).kind, Kind.ohko)
        self.assertEqual(calcMove(self.genMove(name='Horn Drill'), self.genPkmn(), self.genPkmn(), self.genEnv()).kind, Kind.ohko)
        self.assertNotEqual(calcMove(self.genMove(name='Seismic Toss'), self.genPkmn(), self.genPkmn(), self.genEnv()).kind, Kind.ohko)

    def test_move_frustration(self):
        p1 = self.genPkmn(stats=self.genStats(ATK=79), type1='water')
        p2 = self.genPkmn(stats=self.genStats(DEF=163))
        p1.happiness = 68
        m = self.genMove(name='Frustration', power=42) # power should be ignored
        self.assertEqual(calcMove(m, p1, p2, self.genEnv()).damage, self.getDamage((255 - 68) / 2.5, 79, 163))

    def test_move_return(self):
        p1 = self.genPkmn(stats=self.genStats(ATK=133), type1='water')
        p2 = self.genPkmn(stats=self.genStats(DEF=201))
        p1.happiness = 82
        m = self.genMove(name='Return', power=14) # power should be ignored
        self.assertEqual(calcMove(m, p1, p2, self.genEnv()).damage, self.getDamage(82 / 2.5, 133, 201))

    def test_move_grass_knot(self):
        p1 = self.genPkmn(stats=self.genStats(ATK=99), type1='water')
        p2 = self.genPkmn(stats=self.genStats(DEF=166))
        m = self.genMove(name='Grass Knot')
        p2.weight = 59
        self.assertEqual(calcMove(m, p1, p2, self.genEnv()).damage, self.getDamage(80, 99, 166))
        p2.weight = 0.6
        self.assertEqual(calcMove(m, p1, p2, self.genEnv()).damage, self.getDamage(20, 99, 166))
        p2.weight = 187
        self.assertEqual(calcMove(m, p1, p2, self.genEnv()).damage, self.getDamage(100, 99, 166))
        p2.weight = 347
        self.assertEqual(calcMove(m, p1, p2, self.genEnv()).damage, self.getDamage(120, 99, 166))
        p2.weight = 0.012
        self.assertNotEffective(calcMove(m, p1, p2, self.genEnv()))

    def test_move_gyro_ball(self):
        p1 = self.genPkmn(stats=self.genStats(ATK=99, SPE=204), type1='ground')
        p2 = self.genPkmn(stats=self.genStats(DEF=166, SPE=172))
        m = self.genMove(name='Gyro Ball')
        self.assertEqual(calcMove(m, p1, p2, self.genEnv()).damage, self.getDamage(25 * (172 / 204), 99, 166))
        p1.SPE.stageAdd(2)
        self.assertEqual(calcMove(m, p1, p2, self.genEnv()).damage, self.getDamage(25 * (172 / 408), 99, 166))
        p2.SPE.stageAdd(3)
        self.assertEqual(calcMove(m, p1, p2, self.genEnv()).damage, self.getDamage(25 * (430 / 408), 99, 166))

    def test_move_low_kick(self):
        p1 = self.genPkmn(stats=self.genStats(ATK=99), type1='water')
        p2 = self.genPkmn(stats=self.genStats(DEF=166))
        m = self.genMove(name='Low Kick')
        p2.weight = 59
        self.assertEqual(calcMove(m, p1, p2, self.genEnv()).damage, self.getDamage(80, 99, 166))
        p2.weight = 0.6
        self.assertEqual(calcMove(m, p1, p2, self.genEnv()).damage, self.getDamage(20, 99, 166))
        p2.weight = 187
        self.assertEqual(calcMove(m, p1, p2, self.genEnv()).damage, self.getDamage(100, 99, 166))
        p2.weight = 347
        self.assertEqual(calcMove(m, p1, p2, self.genEnv()).damage, self.getDamage(120, 99, 166))
        p2.weight = 0.012
        self.assertNotEffective(calcMove(m, p1, p2, self.genEnv()))

    def test_move_magnitude(self):
        m = self.genMove(name='Magnitude')
        p1 = self.genPkmn(type1='rock', stats=self.genStats(ATK=222))
        p2 = self.genPkmn(stats=self.genStats(DEF=333))
        damage = (self.getDamage(10, 222, 333)[0], self.getDamage(150, 222, 333)[1])
        self.assertEqual(calcMove(m, p1, p2, self.genEnv()).damage, damage)

    def test_move_night_shade(self):
        m = self.genMove(name='Night Shade')
        p1 = self.genPkmn()
        self.assertEqual(calcMove(m, p1, self.genPkmn(), self.genEnv()).damage, (100, 100))
        p1.level=57
        self.assertEqual(calcMove(m, p1, self.genPkmn(), self.genEnv()).damage, (57, 57))
    
    def test_move_seismic_toss(self):
        m = self.genMove(name='Seismic Toss')
        p2 = self.genPkmn()
        self.assertEqual(calcMove(m, self.genPkmn(), p2, self.genEnv()).damage, (100, 100))
        p2.level=39
        self.assertEqual(calcMove(m, self.genPkmn(), p2, self.genEnv()).damage, (39, 39))

    def test_move_psywave(self):
        self.assertEqual(calcMove(self.genMove(name='Psywave'), self.genPkmn(), self.genPkmn(), self.genEnv()).damage, (50, 150))

    def test_move_punishment(self):
        p1 = self.genPkmn(stats=self.genStats(ATK=85), type1='dark')
        p2 = self.genPkmn(stats=self.genStats(DEF=165, ATK=123, SPD=245, SPE=201))
        m = self.genMove(name='Punishment')
        self.assertEqual(calcMove(m, p1, p2, self.genEnv()).damage, self.getDamage(60, 85, 165))
        p1.DEF.stageAdd(1)
        p2.ATK.stageAdd(1)
        p2.SPD.stageAdd(1)
        self.assertEqual(calcMove(m, p1, p2, self.genEnv()).damage, self.getDamage(100, 85, 165))
        p2.SPD.stageAdd(1)
        p2.SPE.stageAdd(-1)
        self.assertEqual(calcMove(m, p1, p2, self.genEnv()).damage, self.getDamage(120, 85, 165))
        p2.SPD.stageAdd(-2)
        p2.SPE.stageAdd(2)
        self.assertEqual(calcMove(m, p1, p2, self.genEnv()).damage, self.getDamage(100, 85, 165))

    def test_move_smelling_salts(self):
        m = self.genMove(name='Smelling Salts', power=60)
        p1 = self.genPkmn(stats=self.genStats(ATK=154), type1='dark')
        p2 = self.genPkmn(stats=self.genStats(DEF=235))
        self.assertEqual(calcMove(m, p1, p2, self.genEnv()).damage, self.getDamage(60, 154, 235))
        p2.status='par'
        self.assertEqual(calcMove(m, p1, p2, self.genEnv()).damage, self.getDamage(120, 154, 235))

    def test_move_sonic_boom(self):
        self.assertEqual(calcMove(self.genMove(name='Sonic Boom'), self.genPkmn(), self.genPkmn(), self.genEnv()).damage, (20, 20))

    def test_move_thunder(self):
        m = self.genMove(name='Thunder', accuracy=70)
        self.assertEqual(calcMove(m, self.genPkmn(), self.genPkmn(), self.genEnv()).accuracy, 70)
        self.assertEqual(calcMove(m, self.genPkmn(), self.genPkmn(), self.genEnv(weather='rain')).accuracy, 100)
        
    def test_move_triple_kick(self):
        # 3 hits with 10, 20, 30 base power
        m = self.genMove(name="Triple Kick", power=10, type='fighting')
        p1 = self.genPkmn(stats=self.genStats(ATK=190))
        p2 = self.genPkmn(stats=self.genStats(DEF=173), type1='normal')
        dmg1 = self.getDamage(10, 190, 173, 2)[0]
        dmg2 = self.getDamage(10, 190, 173, 2)[1] + self.getDamage(20, 190, 173, 2)[1] + self.getDamage(30, 190, 173, 2)[1]
        self.assertEqual(calcMove(m, p1, p2, self.genEnv()).damage, (dmg1, dmg2))
        
    def test_move_weather_ball(self):
        p1 = self.genPkmn(stats=self.genStats(ATK=70))
        p2 = self.genPkmn(stats=self.genStats(DEF=80))
        m = self.genMove(name='Weather Ball', power=50)
        e = self.genEnv()
        self.assertEqual(calcMove(m, p1, p2, e).damage, self.getDamage(50, 70, 80, 1.5))
        e.weather = 'sun'
        self.assertEqual(calcMove(m, p1, p2, e).damage, self.getDamage(100, 70, 80, 1))
        self.assertEqual(calcMove(m, p1, p2, e).move.type, 'fire')
        e.weather = 'rain'
        self.assertEqual(calcMove(m, p1, p2, e).damage, self.getDamage(100, 70, 80, 1))
        self.assertEqual(calcMove(m, p1, p2, e).move.type, 'water')
        e.weather = 'hail'
        self.assertEqual(calcMove(m, p1, p2, e).damage, self.getDamage(100, 70, 80, 1))
        self.assertEqual(calcMove(m, p1, p2, e).move.type, 'ice')
        e.weather = 'sandstorm'
        self.assertEqual(calcMove(m, p1, p2, e).damage, self.getDamage(100, 70, 80, 1))
        self.assertEqual(calcMove(m, p1, p2, e).move.type, 'rock')
        e.weather = 'fog'
        self.assertEqual(calcMove(m, p1, p2, e).damage, self.getDamage(100, 70, 80, 1.5))
        self.assertEqual(calcMove(m, p1, p2, e).move.type, 'normal')
    
    
    def test_json1(self):
        p1 = self.genPkmn(moves=[self.genMove(category=MoveCategory.nonDamaging), self.genMove(category=MoveCategory.special)])
        dic = buildDictSetup(p1, self.genPkmn(), self.genEnv())
        self.assertEqual(json.dumps(dic, sort_keys=True), '{"blue": [{"accuracy": 100, "damage": null, "eff": "normal", "kind": "status"}, {"accuracy": 100, "damage": [109.64999999999999, 129.0], "eff": "normal", "kind": "normal"}], "red": [{"accuracy": 100, "damage": [109.64999999999999, 129.0], "eff": "normal", "kind": "normal"}]}')
    

if __name__ == '__main__':
    unittest.main()
    
